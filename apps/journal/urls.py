from django.urls import path
from . import views

app_name = "journal"

urlpatterns = [
    path("", views.journal_list, name="list"),
    path("new/", views.journal_create, name="create"),
    path("delete/<int:entry_id>/", views.journal_delete, name="delete"),
    path("undo/", views.journal_restore, name="restore"),
    path("trash/", views.journal_trash, name="trash"),
    path("hard-delete/<int:entry_id>/", views.journal_hard_delete, name="hard_delete"),
]
