# Generated by Django 4.2.11 on 2024-06-01 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("chat", "0008_alter_image_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="image",
            name="image",
            field=models.ImageField(
                default="",
                upload_to="D:\\Machine Learning Projects\\DermIT\\web-app\\dermit-backend\\chat\\Images\\Input",
            ),
        ),
    ]