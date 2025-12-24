from django.urls import path
from . import views

app_name = "faith"

urlpatterns = [
    path("", views.index, name="index"),
    path("scripture/", views.scripture_lookup, name="scripture"),
    path("stories/", views.stories, name="stories"),
    path("stories/<slug:slug>/",views.story_detail,name="story_detail",),
]

