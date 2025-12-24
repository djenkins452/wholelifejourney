from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST



from .forms import ProfileForm
from .models import Module, UserModule

# --------------------------------------------------
# DASHBOARD
# --------------------------------------------------
from core.services.dashboard_tiles.journal import build_journal_tile
from core.services.dashboard_tiles.health_weight import build_health_weight_tile
from core.services.dashboard_tiles.health_fasting import build_health_fasting_tile

def public_home(request):
    if request.user.is_authenticated:
        return redirect("core:dashboard")
    return render(request, "public/home.html")


def about(request):
    return render(request, "public/about.html")


@login_required
def dashboard(request):
    tiles = [
        build_journal_tile(request.user),
        build_health_weight_tile(request.user),
        build_health_fasting_tile(request.user),
    ]


    return render(
        request,
        "core/dashboard.html",
        {
            "tiles": tiles,
        },
    )



# --------------------------------------------------
# PROFILE
# --------------------------------------------------

@login_required
@require_POST
def profile(request):
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
    Enable / disable APP-LEVEL modules only.
    Server returns authoritative enabled_module_keys.
    """
    enabled_keys = set(request.POST.getlist("modules"))

    app_module_keys = [
        "faith",
        "journaling",
        "health",
        "mental",
        "life",
        "finance",
        "relationships",
        "learning",
        "goals",
    ]

    app_modules = Module.objects.filter(key__in=app_module_keys)

    final_enabled = []

    for module in app_modules:
        user_module, _ = UserModule.objects.get_or_create(
            user=request.user,
            module=module,
        )
        user_module.is_enabled = module.key in enabled_keys
        user_module.save()

        if user_module.is_enabled:
            final_enabled.append(module.key)

    return JsonResponse({
        "status": "ok",
        "enabled_module_keys": final_enabled,
    })
