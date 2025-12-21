from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path("dashboard/", views.dashboard, name="dashboard"),
    path("settings/modules/", views.module_settings, name="module_settings"),
]
