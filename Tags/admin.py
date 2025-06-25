from django.contrib import admin
from django.contrib import admin
from .models import Blog, Tag ,Blog_Header
from django.utils.html import strip_tags

class Blog_admin(admin.ModelAdmin):
    list_display = ('title','content','tags','created_at','images','slugs',)

    admin.site.register(Blog)

class blog_header_admin(admin.ModelAdmin):
    list_display = ("blog_title", "blog_des")  # <-- Use the method name

admin.site.register(Blog_Header,blog_header_admin)

admin.site.register(Tag)

# Register your models here.
