# Generated by Django 5.1.3 on 2024-11-15 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("admin_custom", "0002_alter_project_category"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="project_image",
            field=models.ImageField(blank=True, null=True, upload_to="images/"),
        ),
    ]
