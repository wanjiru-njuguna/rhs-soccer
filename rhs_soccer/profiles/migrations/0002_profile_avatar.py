# Generated by Django 4.2.13 on 2024-07-09 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='avatars/', verbose_name='Avatar'),
        ),
    ]
