from django.contrib import admin

from .models import Report

# Register your models here.

@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'origin', 'author', 'progress', 'created_at', 'updated_at')
    list_filter = ('type', 'progress', 'created_at', 'updated_at')
    search_fields = ('id', 'type', 'origin__pk', 'author__username', 'progress', 'created_at', 'updated_at')
    ordering = ('-created_at',)
