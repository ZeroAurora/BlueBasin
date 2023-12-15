from django.db import models

from bluebasin.apps.user.models import User
from bluebasin.apps.forum.models import Post


class Report(models.Model):
    class Type(models.IntegerChoices):
        OTHER = 0
        ILLEGAL_CONTENT = 1
        SPAM = 2
        HARASSMENT = 3
        HATE_SPEECH = 4
        VIOLENCE = 5
        DELETE_MY_POST = 6

    class Progress(models.IntegerChoices):
        OPEN = 0
        IN_PROGRESS = 1
        CLOSED = 2

    type = models.IntegerField(choices=Type.choices, default=Type.OTHER)
    detail = models.TextField(blank=True)
    origin = models.ForeignKey(Post, related_name="reports", on_delete=models.CASCADE)
    author = models.ForeignKey(User, related_name="reports", on_delete=models.CASCADE)
    progress = models.IntegerField(choices=Progress.choices, default=Progress.OPEN)
    reply = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Report #{self.id}'
