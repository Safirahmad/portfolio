from django.contrib import admin

from social.models import socail_media ,social_header

class social_admin(admin.ModelAdmin):
    list_display = ("social_image","socila_link")


admin.site.register(socail_media,social_admin)
admin.site.register(social_header)
# Register your models here.
