from django.contrib import admin
from .models import JournalEntry


@admin.register(JournalEntry)
class JournalEntryAdmin(admin.ModelAdmin):
    list_display = ("user", "created_at", "deleted_at")
    list_filter = ("created_at", "deleted_at")
    search_fields = ("body",)

