from django.db import migrations


def add_app_modules(apps, schema_editor):
    Module = apps.get_model("core", "Module")

    # App-level modules only (sub-apps inherit from parent)
    app_modules = [
        ("faith", "Faith", 5),
        ("journal", "Journal", 10),
        ("health", "Health", 20),
        ("mental", "Mental", 30),
        ("life", "Life", 40),
        ("finance", "Finance", 50),
        ("relationships", "Relationships", 60),
        ("learning", "Learning", 70),
        ("goals", "Goals", 80),
    ]

    for key, name, sort_order in app_modules:
        Module.objects.get_or_create(
            key=key,
            defaults={
                "name": name,
                "is_active_globally": True,
                "sort_order": sort_order,
            },
        )


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0007_userprofile_display_name"),
    ]

    operations = [
        migrations.RunPython(add_app_modules),
    ]
