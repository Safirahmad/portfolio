# Generated by Django 5.2.1 on 2025-06-23 13:11

import tinymce.models
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("projects", "0005_project_auto_slug"),
    ]

    operations = [
        migrations.CreateModel(
            name="Project_header",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("header_title", models.CharField(max_length=50)),
                ("header_des", tinymce.models.HTMLField()),
            ],
        ),
    ]
