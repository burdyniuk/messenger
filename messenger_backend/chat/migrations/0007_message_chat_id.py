# Generated by Django 3.2.4 on 2022-05-06 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0006_alter_message_from_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='chat_id',
            field=models.IntegerField(default=0),
        ),
    ]
