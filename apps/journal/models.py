from django.conf import settings
from django.db import models
from django.utils import timezone


def default_title():
    return timezone.now().strftime("%A, %b %d, %Y %I:%M %p")


class JournalEntry(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="journal_entries"
    )

    title = models.CharField(
        max_length=255,
        default=default_title,
        blank=True,
    )

    body = models.TextField()

    # NEW: date the entry is about (editable)
    entry_date = models.DateTimeField(default=timezone.now)

    # system timestamp (do not edit)
    created_at = models.DateTimeField(auto_now_add=True)

    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ["-entry_date"]

    def soft_delete(self):
        self.deleted_at = timezone.now()
        self.save(update_fields=["deleted_at"])

    def restore(self):
        self.deleted_at = None
        self.save(update_fields=["deleted_at"])

    def __str__(self):
        return self.title
