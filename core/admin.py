from django.contrib import admin
from .models import Module, UserModule


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ("name", "key", "is_active_globally", "sort_order")
    list_filter = ("is_active_globally",)
    search_fields = ("name", "key")
    ordering = ("sort_order", "name")


@admin.register(UserModule)
class UserModuleAdmin(admin.ModelAdmin):
    list_display = ("user", "module", "is_enabled", "enabled_at")
    list_filter = ("is_enabled", "module")
    search_fields = ("user__username", "user__email", "module__key")

