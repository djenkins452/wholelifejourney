from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    # Public
    path("", views.public_home, name="public_home"),

    # App (authenticated)
    path("app/", views.dashboard, name="dashboard"),

    # Profile / Settings (EXISTING, REQUIRED)
    path("profile/", views.profile, name="profile"),
    path("settings/modules/", views.module_settings, name="module_settings"),
]
