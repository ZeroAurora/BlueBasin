from django.apps import AppConfig


class BBAdminConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "bluebasin.apps.admin"
    label = "bb_admin"
