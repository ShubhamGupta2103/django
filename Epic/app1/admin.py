from django.contrib import admin
from .models import Image, Tag

# Register your models here.
@admin.register(Tag)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

