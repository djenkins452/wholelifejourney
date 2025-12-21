from django.conf import settings
from django.db import models

class Module(models.Model):
    """
    A module is a feature area like Journaling, Fasting, Weight, etc.
    """
    key = models.SlugField(unique=True)  # ex: "journaling"
    name = models.CharField(max_length=100)  # ex: "Journaling"
    description = models.TextField(blank=True)
    is_active_globally = models.BooleanField(default=True)  # admin kill-switch
    sort_order = models.PositiveIntegerField(default=100)

    class Meta:
        ordering = ["sort_order", "name"]

    def __str__(self) -> str:
        return f"{self.name} ({self.key})"


class UserModule(models.Model):
    """
    Per-user module enablement.
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    is_enabled = models.BooleanField(default=False)
    enabled_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        unique_together = ("user", "module")

    def __str__(self) -> str:
        return f"{self.user} -> {self.module.key}: {self.is_enabled}"
