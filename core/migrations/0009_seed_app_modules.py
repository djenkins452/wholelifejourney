from django.db import migrations


def seed_app_modules(apps, schema_editor):
    Module = apps.get_model("core", "Module")

    modules = [
        ("faith", "Faith"),
        ("journaling", "Journaling"),
        ("health", "Health"),
        ("mental", "Mental"),
        ("life", "Life"),
        ("finance", "Finance"),
        ("relationships", "Relationships"),
        ("learning", "Learning"),
        ("goals", "Goals"),
    ]

    for key, name in modules:
        Module.objects.get_or_create(
            key=key,
            defaults={"name": name}
        )


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0008_add_app_modules"),
    ]

    operations = [
        migrations.RunPython(seed_app_modules),
    ]
