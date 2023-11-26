from django.contrib import admin

from .models import Identity

@admin.register(Identity)
class IdentityAdmin(admin.ModelAdmin):
    list_display = ["name", "user"]
    search_fields = ["name", "user"]