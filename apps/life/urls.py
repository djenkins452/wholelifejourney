from django.urls import path
from . import views

app_name = "life"

urlpatterns = [
    path("", views.life_index, name="index"),
]
