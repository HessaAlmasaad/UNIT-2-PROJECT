# Generated by Django 5.1.3 on 2024-11-19 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("admin_custom", "0008_alter_project_role_details_projectimage"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="project_image",
            field=models.ImageField(default="images/defualt.jpg", upload_to="images/"),
        ),
    ]