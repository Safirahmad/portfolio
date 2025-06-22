from django.db import models
from tinymce.models import HTMLField

from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model



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

class skills(models.Model):
    User = get_user_model()
    skill_text= models.CharField(max_length=50)
    skill_image = models.ImageField(upload_to='skills')
    created_at = models.DateTimeField(auto_now_add=True , null=True ,  blank= True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.skill_text
    

# Create your models here.
