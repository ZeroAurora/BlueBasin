from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="forum_index"),
    path("posts/", views.posts_index),
    path("posts/create/", views.posts_create, name="forum_posts_create"),
    path("posts/<int:post_id>/", views.posts_view, name="forum_posts_view"),
]
