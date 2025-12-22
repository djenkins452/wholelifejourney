from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path("dashboard/", views.dashboard, name="dashboard"),
    path("settings/modules/", views.module_settings, name="module_settings"),

    # Profile (modal save endpoint)
    path("profile/", views.profile_view, name="profile"),

    # Journal routes have been migrated to apps.journal
    # path("journal/", views.journal_list, name="journal_list"),
    # path("journal/new/", views.journal_create, name="journal_create"),
    # path("journal/delete/<int:entry_id>/", views.journal_delete, name="journal_delete"),
    # path("journal/undo/", views.journal_restore, name="journal_restore"),
    # path("journal/trash/", views.journal_trash, name="journal_trash"),
    # path("journal/hard-delete/<int:entry_id>/", views.journal_hard_delete, name="journal_hard_delete"),
]
