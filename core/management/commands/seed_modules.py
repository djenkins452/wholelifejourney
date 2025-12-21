from django.core.management.base import BaseCommand
from core.models import Module

DEFAULT_MODULES = [
    ("journaling", "Journaling", "Daily entries and AI reflections", 10),
    ("fasting", "Fasting", "Track fasting windows and consistency", 20),
    ("weight", "Weight", "Track weight trend over time", 30),
    ("food", "Food", "Food log and patterns (simple)", 40),
    ("glucose", "Blood Glucose", "Manual entry or future CGM sync", 50),
    ("blood_pressure", "Blood Pressure", "Readings + trends", 60),
    ("heart_rate", "Heart Rate", "Resting HR and trends", 70),
    ("workouts", "Workouts", "Resistance + cardio logging", 80),
]

class Command(BaseCommand):
    help = "Seed default modules"

    def handle(self, *args, **options):
        created = 0
        updated = 0

        for key, name, desc, sort in DEFAULT_MODULES:
            obj, was_created = Module.objects.update_or_create(
                key=key,
                defaults={
                    "name": name,
                    "description": desc,
                    "sort_order": sort,
                    "is_active_globally": True,
                },
            )
            if was_created:
                created += 1
            else:
                updated += 1

        self.stdout.write(self.style.SUCCESS(
            f"Modules seeded. Created: {created}, Updated: {updated}"
        ))
