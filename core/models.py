from django.conf import settings
from django.db import models
from django.utils import timezone


class UserProfile(models.Model):
    """
    One profile per user for global preferences
    """
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="profile"
    )

    display_name = models.CharField(
        max_length=100,
        blank=True,
        help_text="Name shown throughout the app (falls back to full name or username)"
    )

    timezone = models.CharField(
        max_length=50,
        default="UTC",
        help_text="IANA time zone, e.g. America/New_York"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_display_name(self):
        """
        Best-available human name for UI and AI interactions
        """
        if self.display_name:
            return self.display_name

        full_name = self.user.get_full_name()
        if full_name:
            return full_name

        return self.user.username

    def __str__(self):
        return f"Profile for {self.user}"


class Module(models.Model):
    """
    Master list of available modules (journaling, fasting, weight, etc.)
    """
    key = models.SlugField(unique=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    is_active_globally = models.BooleanField(default=True)
    sort_order = models.PositiveIntegerField(default=100)

    class Meta:
        ordering = ["sort_order", "name"]

    def __str__(self):
        return f"{self.name} ({self.key})"


class UserModule(models.Model):
    """
    Per-user enable/disable state for each module
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    is_enabled = models.BooleanField(default=False)
    enabled_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        unique_together = ("user", "module")

    def __str__(self):
        return f"{self.user} → {self.module.key}: {self.is_enabled}"
