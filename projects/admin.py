from django.contrib import admin
from .models import Project, ProjectImage, Category ,Project_Header

class ProjectImageInline(admin.TabularInline):  # or StackedInline
    model = ProjectImage
    extra = 1

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title','description','category','created_at','author','live_url','auto_slug')
    inlines = [ProjectImageInline]  
    list_filter = ('category', 'created_at', 'author','auto_slug')
    search_fields = ("title","body")
    raw_id_fields = ("author",)
    date_hierarchy = "created_at"

class header_project_admin(admin.ModelAdmin):
    list_display = ('header_title','header_des')

admin.site.register(Project, ProjectAdmin)
admin.site.register(Category)
admin.site.register(Project_Header,header_project_admin)


# Register your models here.
