# Generated by Django 5.2.1 on 2025-06-19 12:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Tags", "0005_blog_images"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="images",
            field=models.ImageField(
                blank=True, default=None, null=True, upload_to="blogs/"
            ),
        ),
    ]
