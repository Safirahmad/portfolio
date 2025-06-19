from django.contrib import admin


# admin.py
from django.contrib import admin
from .models import Blog, Tag
class Blog_admin(admin.ModelAdmin):
    list_display = ('title','content','tags','created_at','images','slugs',)

    admin.site.register(Blog)
admin.site.register(Tag)

# Register your models here.
