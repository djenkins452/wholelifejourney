# apps/faith/services/verse_of_day.py
from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from typing import Tuple

from django.core.cache import cache
from django.utils import timezone

from .bible_api import get_verse_range


@dataclass(frozen=True)
class VerseOfDay:
    reference: str
    translation_id: str
    book_id: str
    chapter: int
    start_verse: int
    end_verse: int
    text: str


# Phase 1: a curated, uplifting rotation (deterministic by day).
# Later we can make this configurable per user.
ROTATION = [
    # (reference label, translation, book_id, chapter, start, end)
    ("Psalm 23:1", "KJV", "PSA", 23, 1, 1),
    ("Proverbs 3:5–6", "KJV", "PRO", 3, 5, 6),
    ("Isaiah 41:10", "KJV", "ISA", 41, 10, 10),
    ("Matthew 11:28", "KJV", "MAT", 11, 28, 28),
    ("Romans 8:28", "KJV", "ROM", 8, 28, 28),
    ("Philippians 4:6–7", "KJV", "PHP", 4, 6, 7),
]


def _pick_for_today() -> Tuple[str, str, str, int, int, int]:
    today = timezone.localdate()
    idx = (today.toordinal() % len(ROTATION))
    return ROTATION[idx]


def get_verse_of_day() -> VerseOfDay:
    today = timezone.localdate()
    cache_key = f"faith:votd:{today.isoformat()}"
    cached = cache.get(cache_key)
    if cached:
        return cached

    ref, translation_id, book_id, chapter, start, end = _pick_for_today()
    payload = get_verse_range(translation_id, book_id, chapter, start, end)

    # If the API doesn't have that translation ID (or returns empty), fall back to BSB
    if not payload.get("verses"):
        translation_id = "BSB"
        payload = get_verse_range(translation_id, book_id, chapter, start, end)


    verses = payload.get("verses", [])
    text = " ".join([v.get("text", "").strip() for v in verses]).strip()

    out = VerseOfDay(
        reference=ref,
        translation_id=translation_id,
        book_id=book_id,
        chapter=chapter,
        start_verse=start,
        end_verse=end,
        text=text or "(Verse text unavailable)",
    )
    cache.set(cache_key, out, 24 * 60 * 60)
    return out
