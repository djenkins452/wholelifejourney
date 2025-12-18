from django.urls import path, include
from . import views
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', LogoutView.as_view(next_page='/'),name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),

    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('register/', views.register_view, name='register'),

    path('tables/', views.tables_view, name='tables'),
    path('charts/', views.charts_view, name='charts'),
    path('buttons/', views.buttons_view, name='buttons'),
    path('cards/', views.cards_view, name='cards'),   # ← missing before
    path('blank/', views.blank_view, name='blank'),

    path('forgot-password/', views.forgot_password_view, name='forgot_password'),

    path('utilities_animation/', views.utilities_animation_view, name='utilities_animation'),
    path('utilities_border/', views.utilities_border_view, name='utilities_border'),
    path('utilities_color/', views.utilities_color_view, name='utilities_color'),
    path('utilities_other/', views.utilities_other_view, name='utilities_other'),



]

