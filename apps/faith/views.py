from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .services.verse_of_day import get_verse_of_day
from .services.bible_api import get_available_translations, get_verse_range
from .services.stories import get_stories, get_not_everyone_knows_guidance





@login_required
def faith_index(request):
    return render(request, "faith/index.html")

@login_required
def index(request):
    votd = get_verse_of_day()
    return render(request, "faith/index.html", {"votd": votd})


@login_required
def scripture_lookup(request):
    # Phase 1: offer a small curated subset to keep UI simple.
    # Later we can expand or allow full list.
    all_translations = get_available_translations()

    allowed_ids = {"KJV", "BSB", "WEB"}  # safe starters; expand later after you confirm preferences
    translations = [t for t in all_translations if t.id in allowed_ids]
    if not translations:
        translations = all_translations[:10]

    selected_translation = request.GET.get("t") or (translations[0].id if translations else "KJV")
    book_id = (request.GET.get("b") or "").strip().upper()
    chapter = request.GET.get("c") or ""
    verse_range = (request.GET.get("v") or "").strip()

    passage = None
    passage_title = ""

    if book_id and chapter and verse_range:
        try:
            ch = int(chapter)
            if "-" in verse_range:
                start_s, end_s = verse_range.split("-", 1)
                start_v = int(start_s.strip())
                end_v = int(end_s.strip())
            else:
                start_v = end_v = int(verse_range.strip())

            passage = get_verse_range(selected_translation, book_id, ch, start_v, end_v)
            passage_title = f"{book_id} {ch}:{start_v}" if start_v == end_v else f"{book_id} {ch}:{start_v}-{end_v}"
        except Exception:
            passage = None
            passage_title = "Unable to lookup that reference. Double-check Book ID, chapter, and verse range."

    context = {
        "translations": translations,
        "selected_translation": selected_translation,
        "book_id": book_id,
        "chapter": chapter,
        "verse_range": verse_range,
        "passage": passage,
        "passage_title": passage_title,
    }
    return render(request, "faith/scripture.html", context)


@login_required
def stories(request):
    query = (request.GET.get("q") or "").strip().lower()

    all_stories = get_stories()

    if query:
        stories = [
            s for s in all_stories
            if query in s.title.lower()
            or query in s.story.lower()
            or query in s.why_it_matters.lower()
        ]
    else:
        stories = all_stories

    context = {
        "stories": stories,
        "query": query,
        "tips": get_not_everyone_knows_guidance(),
    }
    return render(request, "faith/stories.html", context)

@login_required
def story_detail(request, slug):
    stories = get_stories()

    story = next(
        (s for s in stories if s.slug == slug),
        None
    )

    if not story:
        raise Http404("Story not found")

    return render(
        request,
        "faith/story_detail.html",
        {"story": story}
    )
