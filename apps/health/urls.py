from django.urls import path
from . import views

app_name = "health"

urlpatterns = [
    path("", views.health_index, name="index"),

    # Weight
    path("weight/", views.weight_list, name="weight_list"),
    path("weight/delete/<int:entry_id>/", views.weight_delete, name="weight_delete"),

    # Fasting (manual entry only)
    path("fasting/", views.fasting_list, name="fasting_list"),
]
