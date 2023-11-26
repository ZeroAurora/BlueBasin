from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("markdown/", views.markdown, name="markdown"),
    path("welcome/", views.welcome, name="welcome"),
    path("code_of_conduct/", views.code_of_conduct, name="code_of_conduct"),
    path("terms/", views.terms, name="terms"),
]
