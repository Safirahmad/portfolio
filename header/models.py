from django.db import models


    
class cv(models.Model):
    cvs = models.FileField(upload_to='cv')


class SiteSettings(models.Model):
    logs = models.FileField(upload_to='logo', blank=True, null=True)


# Create your models here.
