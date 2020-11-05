from django.contrib import admin

from .models import UploadImage


@admin.register(UploadImage)
class UploadImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'image', 'uploaded_at']
    date_hierarchy = 'uploaded_at'