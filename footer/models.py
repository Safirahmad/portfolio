from django.db import models
from django.db import models

class Footer(models.Model):
    logo = models.ImageField(upload_to='logo')
    footer_about = models.TextField()
    footer_location = models.TextField(max_length=50)
    email = models.EmailField()
    linkedin_url = models.URLField(blank=True)
    instagram_url = models.URLField(blank=True)
    youtube_url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)
    copyright = models.CharField(max_length=255)

    def __str__(self):
        return "Footer Content"

# Create your models here.
