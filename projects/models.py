from django.db import models
from datetime import date
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from autoslug import AutoSlugField

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = HTMLField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='project_posts')
    live_url = models.URLField(blank=True, null=True)  
    auto_slug = AutoSlugField(populate_from='title',unique=True , null=True , blank=True)

    def __str__(self):
        return self.title

class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='project_images/')


    def __str__(self):
        return f"Image for {self.project.title}"
    
class Project_Header(models.Model):
    header_title = models.CharField(max_length=50)
    header_des = models.TextField()

    def __str__(self):
        return self.header_title
