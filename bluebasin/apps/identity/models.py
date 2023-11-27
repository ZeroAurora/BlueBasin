from secrets import choice
from string import ascii_letters, digits

from django.db import models

from bluebasin.apps.user.models import User


class Identity(models.Model):
    def generate_random_name():
        return "".join(choice(ascii_letters + digits) for _ in range(8))

    user = models.ForeignKey("user.User", on_delete=models.CASCADE, related_name="identities")  # fmt: skip
    name = models.CharField(max_length=255, default=generate_random_name, unique=True)
    remark = models.TextField(blank=True, null=True)
    show_as_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deprecated_at = models.DateTimeField(blank=True, null=True)
