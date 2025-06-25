from django.db import models



class Education(models.Model):
    educ_title = models.CharField(max_length=50, null=True, blank=True)
    educ_des = models.CharField(max_length=50, null=True, blank=True)
    educ_camp = models.CharField(max_length=30, null=True, blank=True)
    educ_camp1 = models.CharField(max_length=30, null=True, blank=True)
    educ_start_date = models.CharField(max_length=40, null=True, blank=True)
    educ_end_date = models.CharField(max_length=40, null=True, blank=True )
    educ_durations = models.CharField(max_length=30, null=True, blank=True )
    educ_certifi = models.CharField(max_length=30, null=True, blank=True)
    educ_camp_id = models.CharField(max_length=30, null=True, blank=True)
    educ_verify = models.URLField(null=True, blank=True)

# Create your models here.
