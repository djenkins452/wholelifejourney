from .models import UserModule

def enabled_modules(request):
    if not request.user.is_authenticated:
        return {"enabled_modules": []}

    modules = (
        UserModule.objects
        .select_related("module")
        .filter(user=request.user, is_enabled=True)
        .order_by("module__name")
    )

    return {
        "enabled_modules": [um.module for um in modules]
    }
