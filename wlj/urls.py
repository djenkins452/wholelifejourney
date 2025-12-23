from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import home

urlpatterns = [
    path("wlj-super-duper/", admin.site.urls),

    path(
        "login/",
        auth_views.LoginView.as_view(template_name="login.html"),
        name="login",
    ),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),

    # Public / core
    path("", home, name="home"),
    path("", include("core.urls")),

    # Journal
    path("journal/", include("apps.journal.urls")),

    # Life pillar modules (Phase B)
    path("health/", include("apps.health.urls")),
    path("mental/", include("apps.mental.urls")),
    path("life/", include("apps.life.urls")),
    path("finance/", include("apps.finance.urls")),
    path("relationships/", include("apps.relationships.urls")),
    path("learning/", include("apps.learning.urls")),
    path("goals/", include("apps.goals.urls")),
    path("faith/", include("apps.faith.urls")),
]
