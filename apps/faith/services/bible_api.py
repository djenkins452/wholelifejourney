# apps/faith/services/bible_api.py
from __future__ import annotations

import json
import urllib.parse
import urllib.request
from dataclasses import dataclass
from typing import Any, Dict, List, Optional

from django.core.cache import cache


BASE_URL = "https://bible.helloao.org/api"


@dataclass(frozen=True)
class Translation:
    id: str
    name: str
    english_name: str
    short_name: str
    language: str


def _fetch_json(url: str, cache_key: str, ttl_seconds: int = 60 * 60) -> Dict[str, Any]:
    cached = cache.get(cache_key)
    if cached:
        return cached

    try:
        req = urllib.request.Request(
            url,
            headers={
                "User-Agent": "WholeLifeJourney/1.0",
                "Accept": "application/json",
            },
        )

        with urllib.request.urlopen(req, timeout=15) as resp:
            raw = resp.read().decode("utf-8").strip()
            if not raw:
                raise ValueError("Empty response body")

            data = json.loads(raw)

        cache.set(cache_key, data, ttl_seconds)
        return data

    except Exception as exc:
        # IMPORTANT:
        # We fail gracefully so the Faith app never crashes
        # External APIs are not guaranteed to be available
        return {}



def get_available_translations(ttl_seconds: int = 24 * 60 * 60) -> List[Translation]:
    """
    Calls: GET https://bible.helloao.org/api/available_translations.json
    """
    url = f"{BASE_URL}/available_translations.json"
    data = _fetch_json(url, "faith:available_translations", ttl_seconds=ttl_seconds)

    out: List[Translation] = []
    for t in data.get("translations", []):
        out.append(
            Translation(
                id=t.get("id", ""),
                name=t.get("name", ""),
                english_name=t.get("englishName", ""),
                short_name=t.get("shortName", ""),
                language=t.get("language", ""),
            )
        )
    return [t for t in out if t.id]


def get_books(translation_id: str) -> Dict[str, Any]:
    url = f"{BASE_URL}/{urllib.parse.quote(translation_id)}/books.json"
    return _fetch_json(url, f"faith:books:{translation_id}", ttl_seconds=24 * 60 * 60)


def get_chapter(translation_id: str, book_id: str, chapter_number: int) -> Dict[str, Any]:
    url = f"{BASE_URL}/{urllib.parse.quote(translation_id)}/{urllib.parse.quote(book_id)}/{chapter_number}.json"
    return _fetch_json(url, f"faith:chapter:{translation_id}:{book_id}:{chapter_number}", ttl_seconds=6 * 60 * 60)


def get_verse_range(
    translation_id: str,
    book_id: str,
    chapter_number: int,
    start_verse: int,
    end_verse: int,
) -> Dict[str, Any]:
    """
    Free Use Bible API returns verses inside:
      chapter -> { content: [ {type:'verse', number:int, content:[...]} , ... ] }
    We extract verse text by concatenating the verse content pieces.
    """
    payload = get_chapter(translation_id, book_id, chapter_number)

    # Defensive: API might be down / return {}
    chapter_obj = (payload or {}).get("chapter", {}) or {}
    content_items = chapter_obj.get("content", []) or []

    picked = []
    for item in content_items:
        if item.get("type") != "verse":
            continue

        try:
            n = int(item.get("number"))
        except Exception:
            continue

        if not (start_verse <= n <= end_verse):
            continue

        # Verse text is usually an array of string fragments in item["content"]
        parts = item.get("content") or []

        lines = []
        if isinstance(parts, list):
            for p in parts:
                # p may be a dict like {"text": "...", "poem": 1}
                if isinstance(p, dict):
                    t = p.get("text", "").strip()
                else:
                    t = str(p).strip()

                if t:
                    lines.append(t)
        else:
            lines.append(str(parts).strip())

        # Join poetic lines with a space, not dict noise
        text = " ".join(lines).replace(" ,", ",").strip()


        picked.append({
            "number": n,
            "text": text,
        })


    return {
        "translation": (payload or {}).get("translation"),
        "book": (payload or {}).get("book"),
        "chapter": chapter_obj.get("number", chapter_number),
        "verses": picked,
    }
