# Generated by Django 4.2.11 on 2024-05-07 03:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_remove_message_response_message_is_response_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='read',
        ),
    ]
