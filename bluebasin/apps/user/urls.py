from django.urls import path

from . import views

urlpatterns = [
    path("settings/", views.settings, name="user_settings"),
    path("settings/info", views.settings_info, name="user_settings_info"),
    path("settings/password", views.settings_password, name="user_settings_password"),
    path("signup/", views.signup, name="user_signup"),
    path("login/", views.login, name="user_login"),
    path("logout/", views.logout, name="user_logout"),
    path("reset_password/", views.reset_password, name="user_reset_password"),
]
