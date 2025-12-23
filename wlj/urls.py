from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView

urlpatterns = [
    path("wlj-super-duper/", admin.site.urls),

    # Auth (canonical)
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="login.html"),
        name="login",
    ),
    path(
        "logout/",
        auth_views.LogoutView.as_view(next_page="/"),
        name="logout",
    ),

    # Public root -> core public home
    # (core.urls already maps "" to views.public_home)
    path("", include("core.urls")),

    # Journal
    path("journal/", include("apps.journal.urls")),

    # Life pillar modules
    path("health/", include("apps.health.urls")),
    path("mental/", include("apps.mental.urls")),
    path("life/", include("apps.life.urls")),
    path("finance/", include("apps.finance.urls")),
    path("relationships/", include("apps.relationships.urls")),
    path("learning/", include("apps.learning.urls")),
    path("goals/", include("apps.goals.urls")),
    path("faith/", include("apps.faith.urls")),
]
