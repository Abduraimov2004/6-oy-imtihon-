# Generated by Django 5.0.8 on 2024-08-07 11:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_photo_liked_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='liked_by',
        ),
    ]
