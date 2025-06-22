from django.contrib import admin
from .models import home_slider, skills

@admin.register(skills)
class skills_admin(admin.ModelAdmin):
    list_display = ("skill_text", "skill_image","created_at")
    list_filter = ("created_at",)
    search_fields = ("skill_text",)  # Make sure these fields exist!
    raw_id_fields = ("author",)
    date_hierarchy = "created_at"
    

admin.site.register(home_slider)

# Register your models here.
