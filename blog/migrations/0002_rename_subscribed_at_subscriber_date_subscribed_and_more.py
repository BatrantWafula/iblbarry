# Generated by Django 5.0.6 on 2024-05-23 11:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subscriber',
            old_name='subscribed_at',
            new_name='date_subscribed',
        ),
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
    ]
