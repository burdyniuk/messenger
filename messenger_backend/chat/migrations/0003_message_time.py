# Generated by Django 3.2.4 on 2022-05-06 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_rename_messages_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
