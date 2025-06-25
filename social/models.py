from django.db import models



class socail_media(models.Model):
    social_image = models.ImageField(upload_to='socilamedia')
    socila_link = models.URLField(blank=True, null=True)

class social_header (models.Model):
    socila_header = models.CharField(max_length=50)
# Create your models here.
