from django.urls import path
from . import views

app_name = "relationships"

urlpatterns = [
    path("", views.relationships_index, name="index"),
]
