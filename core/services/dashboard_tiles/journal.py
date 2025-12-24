from datetime import timedelta

from django.utils import timezone

from apps.journal.models import JournalEntry


def build_journal_tile(user):
    """
    Build dashboard-ready summary data for the Journal tile.

    Rules:
    - Excludes soft-deleted entries
    - Streak is based on entry_date (not created_at)
    - Returns plain data only (no HTML, no formatting)
    """

    now = timezone.now()

    # Base queryset: active entries only
    qs = JournalEntry.objects.filter(
        user=user,
        deleted_at__isnull=True,
    )

    total_entries = qs.count()

    # Hidden = soft-deleted entries
    hidden_entries = JournalEntry.objects.filter(
        user=user,
        deleted_at__isnull=False,
    ).count()

    # -------------------------------
    # Streak calculation
    # -------------------------------
    streak = 0
    current_day = now.date()

    # Get distinct entry dates (date-only)
    entry_dates = (
        qs.values_list("entry_date", flat=True)
        .order_by("-entry_date")
    )

    entry_days = {dt.date() for dt in entry_dates}

    # Walk backward day by day
    while current_day in entry_days:
        streak += 1
        current_day -= timedelta(days=1)

    return {
        "key": "journal",
        "title": "Journal",
        "metrics": {
            "total_entries": total_entries,
            "hidden_entries": hidden_entries,
            "streak_days": streak,
        },
        "cta": {
            "label": "Write today",
            "url": "/journal/",
        },
    }
