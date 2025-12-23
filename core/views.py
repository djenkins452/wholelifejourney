from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from .forms import ProfileForm
from .models import Module, UserModule


def public_home(request):
    """
    Public-facing landing page.
    Logged-in users are redirected to the app dashboard.
    """
    if request.user.is_authenticated:
        return redirect("core:dashboard")

    return render(request, "public/home.html")


@login_required
def dashboard(request):
    """
    Authenticated user's home.
    This is the primary app entry point.
    """
    return render(request, "core/dashboard.html")


# --------------------------------------------------
# PROFILE (Phase C — REQUIRED)
# --------------------------------------------------

@login_required
@require_POST
def profile(request):
    """
    AJAX endpoint to update user profile (timezone, display name, etc).
    """
    profile = request.user.profile
    form = ProfileForm(request.POST, instance=profile)

    if form.is_valid():
        form.save()
        return JsonResponse({"status": "ok"})

    return JsonResponse({"status": "error", "errors": form.errors}, status=400)


@login_required
@require_POST
def module_settings(request):
    """
    AJAX endpoint to enable / disable user modules.
    """
    enabled_keys = set(request.POST.getlist("modules"))

    for module in Module.objects.all():
        user_module, _ = UserModule.objects.get_or_create(
            user=request.user,
            module=module
        )
        user_module.enabled = module.key in enabled_keys
        user_module.save()

    return JsonResponse({"status": "ok"})
