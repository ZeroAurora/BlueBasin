from django.contrib import admin

from .models import *

# admin.site.register(Tag)
# admin.site.register(AvaliableReaction)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["pk", "title", "author", "created_at"]
    search_fields = ["pk", "title", "author", "content"]

# admin.site.register(Reaction)
