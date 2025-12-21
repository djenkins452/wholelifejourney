from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import render, redirect
from django.utils import timezone

from .models import Module, UserModule


@login_required
def dashboard(request):
    modules = Module.objects.filter(is_active_globally=True).order_by("sort_order", "name")
    enabled_map = {
        um.module_id: um.is_enabled
        for um in UserModule.objects.filter(user=request.user)
    }

    enabled_modules = [m for m in modules if enabled_map.get(m.id)]
    disabled_modules = [m for m in modules if not enabled_map.get(m.id)]

    return render(
        request,
        "core/dashboard.html",
        {
            "enabled_modules": enabled_modules,
            "disabled_modules": disabled_modules,
        },
    )


@login_required
def module_settings(request):
    modules = Module.objects.filter(is_active_globally=True).order_by("sort_order", "name")

    # Ensure a UserModule row exists for each module for this user
    existing = {um.module_id: um for um in UserModule.objects.filter(user=request.user)}

    if request.method == "POST":
        posted_keys = set(request.POST.getlist("modules"))  # list of module keys checked

        with transaction.atomic():
            for m in modules:
                um = existing.get(m.id)
                if um is None:
                    um = UserModule.objects.create(user=request.user, module=m, is_enabled=False)

                should_enable = (m.key in posted_keys)

                if should_enable and not um.is_enabled:
                    um.is_enabled = True
                    um.enabled_at = timezone.now()
                    um.save(update_fields=["is_enabled", "enabled_at"])
                elif (not should_enable) and um.is_enabled:
                    um.is_enabled = False
                    um.save(update_fields=["is_enabled"])

        return redirect("core:dashboard")

    # GET
    enabled_keys = set()
    for m in modules:
        um = existing.get(m.id)
        if um and um.is_enabled:
            enabled_keys.add(m.key)

    return render(
        request,
        "core/module_settings.html",
        {
            "modules": modules,
            "enabled_keys": enabled_keys,
        },
    )
