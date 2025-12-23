from .models import Module, UserModule, UserProfile
from .forms import ProfileForm

# =====================================================
# Whole Life Journey — Context Processor (AUTHORITATIVE)
# =====================================================
# Modules = APPS ONLY (user toggleable)
# Sub-areas (like Weight/Fasting) are NOT modules and are NOT toggleable.
# Filtering MUST be done here (Python), never in templates.

APP_MODULE_KEYS = [
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


def enabled_modules(request):
    """
    Global context for:
    - enabled modules (templates)
    - enabled module keys (JS / nav enforcement)
    - profile modal (timezone + modules)

    MUST be defensive: context processors run on every request.
    """
    if not request.user.is_authenticated:
        return {
            "enabled_modules": [],
            "enabled_module_keys": [],
            "modules": [],        # legacy: keep for safety
            "app_modules": [],    # NEW: app-level modules only
            "enabled_keys": set(),
            "profile_form": None,
        }

    # 🔒 GUARANTEE PROFILE EXISTS (critical)
    profile, _ = UserProfile.objects.get_or_create(
        user=request.user,
        defaults={"timezone": "UTC"},
    )

    # Enabled modules for this user
    user_modules = (
        UserModule.objects
        .select_related("module")
        .filter(user=request.user, is_enabled=True)
        .order_by("module__name")
    )

    enabled_modules = [um.module for um in user_modules]
    enabled_module_keys = [um.module.key for um in user_modules]

    enabled_keys = set(enabled_module_keys)

    # All globally available modules (legacy / internal use)
    all_modules = (
        Module.objects
        .filter(is_active_globally=True)
        .order_by("sort_order", "name")
    )

    # ✅ App-level modules only (AUTHORITATIVE list)
    app_modules = (
        Module.objects
        .filter(is_active_globally=True, key__in=APP_MODULE_KEYS)
        .order_by("sort_order", "name")
    )

    profile_form = ProfileForm(instance=profile)

    return {
        "enabled_modules": enabled_modules,          # for templates
        "enabled_module_keys": enabled_module_keys,  # for JS / JSON
        "modules": all_modules,                      # legacy: keep for safety
        "app_modules": app_modules,                  # NEW: templates should use this
        "enabled_keys": enabled_keys,
        "profile_form": profile_form,
    }
