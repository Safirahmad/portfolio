from django.contrib import admin
from .models import Project, ProjectImage, Category

class ProjectImageInline(admin.TabularInline):  # or StackedInline
    model = ProjectImage
    extra = 1

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title','description','category','created_at','author','live_url')
    inlines = [ProjectImageInline]  
    list_filter = ('category', 'created_at', 'author')
    search_fields = ("title","body")
    raw_id_fields = ("author",)
    date_hierarchy = "created_at"


admin.site.register(Project, ProjectAdmin)
admin.site.register(Category)

# Register your models here.
