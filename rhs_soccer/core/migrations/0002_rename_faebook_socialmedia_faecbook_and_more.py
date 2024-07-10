# Generated by Django 4.2.13 on 2024-07-10 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='socialmedia',
            old_name='faebook',
            new_name='faecbook',
        ),
        migrations.AddField(
            model_name='socialmedia',
            name='youtube',
            field=models.URLField(blank=True, verbose_name='YouTube URL'),
        ),
    ]
