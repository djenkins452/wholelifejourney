from django.urls import path
from . import views

app_name = "mental"

urlpatterns = [
    path("", views.mental_index, name="index"),
]
