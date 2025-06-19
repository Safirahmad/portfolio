from django.db import models
from tinymce.models import HTMLField

from django.db import models
from django.core.exceptions import ValidationError

def validate_svg(file):
    if not file.name.endswith('.svg'):
        raise ValidationError('Only SVG files are allowed.')
class home_slider(models.Model):
    slide_first_des = models.CharField(max_length=30)
    slide_name_part_one = models.CharField(max_length=30 ,default=None)
    slide_name_part_two = models.CharField(max_length=30,default=None)
    slide_des = HTMLField()
    slide_image = models.ImageField(upload_to='mainslider')
    slide_icone_one = models.ImageField(upload_to='mainslider')
    slide_icone_two = models.ImageField(upload_to='mainslider')
    slide_icone_one = models.FileField(upload_to='mainslider', validators=[validate_svg])
    slide_icone_two = models.FileField(upload_to='mainslider', validators=[validate_svg])

# Create your models here.
