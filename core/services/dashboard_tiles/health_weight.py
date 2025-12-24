from datetime import timedelta

from django.utils import timezone
from django.db.models import Avg

from apps.health.models import WeightEntry


def build_health_weight_tile(user):
    """
    Build dashboard-ready summary data for the Health → Weight tile.

    Metrics:
    - current weight (most recent)
    - 30-day average trend (if available)
    """

    today = timezone.now().date()

    qs = WeightEntry.objects.filter(user=user)

    latest = qs.order_by("-date").first()
    earliest = qs.order_by("date").first()

    current_weight = latest.weight if latest else None
    starting_weight = earliest.weight if earliest else None

    weight_change = None
    if current_weight is not None and starting_weight is not None:
        weight_change = float(starting_weight - current_weight)


    return {
        "key": "health_weight",
        "title": "Weight",
        "metrics": {
            "starting_weight": float(starting_weight) if starting_weight else None,
            "current_weight": float(current_weight) if current_weight else None,
            "weight_change": weight_change,
        },
        "cta": {
            "label": "Log weight",
            "url": "/health/weight/",
        },
    }

