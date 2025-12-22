from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.views.decorators.http import require_POST
from django.contrib import messages

from .models import Module, UserModule
from .forms import ProfileForm


# --------------------------------------------------
# Dashboard
# --------------------------------------------------

@login_required
def dashboard(request):
    """
    Main dashboard showing enabled and disabled modules for the user.
    """
    modules = Module.objects.filter(
        is_active_globally=True
    ).order_by("sort_order", "name")

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


# --------------------------------------------------
# Module Settings
# --------------------------------------------------

@login_required
def module_settings(request):
    """
    Enable / disable modules per user.
    """
    modules = Module.objects.filter(
        is_active_globally=True
    ).order_by("sort_order", "name")

    # Existing UserModule rows for this user
    existing = {
        um.module_id: um
        for um in UserModule.objects.filter(user=request.user)
    }

    if request.method == "POST":
        posted_keys = set(request.POST.getlist("modules"))

        with transaction.atomic():
            for module in modules:
                um = existing.get(module.id)

                if um is None:
                    um = UserModule.objects.create(
                        user=request.user,
                        module=module,
                        is_enabled=False,
                    )

                should_enable = module.key in posted_keys

                if should_enable and not um.is_enabled:
                    um.is_enabled = True
                    um.enabled_at = timezone.now()
                    um.save(update_fields=["is_enabled", "enabled_at"])

                elif not should_enable and um.is_enabled:
                    um.is_enabled = False
                    um.save(update_fields=["is_enabled"])

        return redirect("core:dashboard")

    # GET request
    enabled_keys = {
        module.key
        for module in modules
        if existing.get(module.id) and existing[module.id].is_enabled
    }

    return render(
        request,
        "core/module_settings.html",
        {
            "modules": modules,
            "enabled_keys": enabled_keys,
        },
    )

# --------------------------------------------------
# Profile (Modal Content)
# --------------------------------------------------

@login_required
def profile_view(request):
    """
    Profile modal content: user preferences (Phase C1 = timezone only)
    """
    profile = request.user.profile

    if request.method == "POST":
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated.")
            # IMPORTANT: no redirect for modal-based UX
    else:
        form = ProfileForm(instance=profile)

    return render(
        request,
        "core/profile_profile.html",
        {
            "form": form,
        },
    )
