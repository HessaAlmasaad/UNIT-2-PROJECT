# Generated by Django 5.1.3 on 2024-11-15 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("admin_custom", "0003_project_project_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="role_details",
            field=models.TextField(default=255),
        ),
    ]