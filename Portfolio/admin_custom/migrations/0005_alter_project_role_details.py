# Generated by Django 5.1.3 on 2024-11-15 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("admin_custom", "0004_project_role_details"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="role_details",
            field=models.TextField(max_length=255),
        ),
    ]
