from django.core.management.base import BaseCommand
from core.models import Module


DEFAULT_MODULES = [
    {
        "key": "journaling",
        "name": "Journaling",
        "description": "Daily journal entries with AI reflections",
        "sort_order": 10,
    },
    {
        "key": "fasting",
        "name": "Fasting",
        "description": "Track fasting windows and consistency",
        "sort_order": 20,
    },
    {
        "key": "weight",
        "name": "Weight",
        "description": "Track weight trends over time",
        "sort_order": 30,
    },
    {
        "key": "food",
        "name": "Food",
        "description": "Log meals and identify patterns",
        "sort_order": 40,
    },
    {
        "key": "glucose",
        "name": "Blood Glucose",
        "description": "Manual glucose tracking and trends",
        "sort_order": 50,
    },
    {
        "key": "blood_pressure",
        "name": "Blood Pressure",
        "description": "Blood pressure readings and history",
        "sort_order": 60,
    },
    {
        "key": "heart_rate",
        "name": "Heart Rate",
        "description": "Resting heart rate and trends",
        "sort_order": 70,
    },
    {
        "key": "workouts",
        "name": "Workouts",
        "description": "Resistance and cardio workout tracking",
        "sort_order": 80,
    },
    {
        "key": "finance",
        "name": "Finance",
        "description": "All things financial",
        "sort_order": 90,
    },
    {
        "key": "mental_health",
        "name": "Mental Health",
        "description": "Mood and emotional status tracking",
        "sort_order": 100,
    },
]


class Command(BaseCommand):
    help = "Seed default application modules"

    def handle(self, *args, **options):
        created = 0
        updated = 0

        for data in DEFAULT_MODULES:
            obj, was_created = Module.objects.update_or_create(
                key=data["key"],
                defaults={
                    "name": data["name"],
                    "description": data["description"],
                    "sort_order": data["sort_order"],
                    "is_active_globally": True,
                },
            )

            if was_created:
                created += 1
            else:
                updated += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Modules seeded. Created: {created}, Updated: {updated}"
            )
        )
