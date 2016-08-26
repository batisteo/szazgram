from django.contrib import admin

from .models import Illustration


@admin.register(Illustration)
class IllustrationAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image_url')
