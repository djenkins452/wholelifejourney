from datetime import timedelta, datetime
from django.utils import timezone
from django.db.models import F
from apps.health.models import Fast


def _fast_duration_hours(fast):
    """
    Calculate fast duration in hours, handling overnight fasts.
    """
    start = datetime.combine(fast.date, fast.start_time)
    end = datetime.combine(fast.date, fast.end_time)

    if end <= start:
        end += timedelta(days=1)

    return (end - start).total_seconds() / 3600


def build_health_fasting_tile(user):
    """
    Build dashboard-ready summary data for the Health → Fasting tile.

    Metrics:
    - total fast entries
    - current streak (days)
    - weekly average fasting duration (hours)
    """

    today = timezone.now().date()

    qs = Fast.objects.filter(user=user)

    total_entries = qs.count()

    # -------------------------------
    # Streak calculation (by date)
    # -------------------------------
    streak = 0
    current_day = today

    # -------------------------------
    # Streak calculation (by completion day)
    # -------------------------------
    streak = 0

    completion_days = set()

    for f in qs:
        # Overnight fast rolls into next day
        if f.end_time <= f.start_time:
            completion_day = f.date + timedelta(days=1)
        else:
            completion_day = f.date

        completion_days.add(completion_day)

    completion_days = sorted(completion_days, reverse=True)

    if completion_days:
        current_day = completion_days[0]

        while current_day in completion_days:
            streak += 1
            current_day -= timedelta(days=1)


    # -------------------------------
    # Weekly average duration
    # -------------------------------
    week_start = today - timedelta(days=7)
    recent_fasts = qs.filter(date__gte=week_start)

    durations = [_fast_duration_hours(f) for f in recent_fasts]

    avg_hours = None
    if durations:
        avg_hours = round(sum(durations) / len(durations), 1)

    return {
        "key": "health_fasting",
        "title": "Fasting",
        "metrics": {
            "total_entries": total_entries,
            "streak_days": streak,
            "weekly_avg_hours": avg_hours,
        },
        "cta": {
            "label": "Log fast",
            "url": "/health/fasting/",
        },
    }
