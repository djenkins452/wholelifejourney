from django.urls import path
from . import views

app_name = "faith"

urlpatterns = [
    path("", views.faith_index, name="index"),
]
