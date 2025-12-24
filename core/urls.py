from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    # Public
    path("", views.public_home, name="public_home"),
    path("about/", views.about, name="about"),

    # App (authenticated)
    path("app/", views.dashboard, name="dashboard"),

    # Profile / Settings
    path("profile/", views.profile, name="profile"),
    path("settings/modules/", views.module_settings, name="module_settings"),
]
