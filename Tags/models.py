from django.db import models
from datetime import date
from autoslug import AutoSlugField
from django.contrib.auth.models import User
from django.utils.html import strip_tags  # ✅ Needed to clean HTML
from tinymce.models import HTMLField

class Tag(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name



class Tag(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name




class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = HTMLField()
    tags = models.ManyToManyField(Tag)
    created_at = models.DateTimeField(auto_now_add=True)
    images = models.ImageField(upload_to='blogs/', null=True, blank=True, default=None)
    
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='blogs')
    
    slugs = AutoSlugField(populate_from='title', unique=True, null=True, blank=True)

    def __str__(self):
        return self.title

    def reading_time(self):
        plain_text = strip_tags(self.content)
        word_count = len(plain_text.split())
        minutes = max(1, round(word_count / 200))
        return f"{minutes} min read"


class Blog_Header(models.Model):

    blog_title = models.CharField(max_length=50)
    blog_des = models.TextField()

    def __str__(self):
        return self.blog_title
