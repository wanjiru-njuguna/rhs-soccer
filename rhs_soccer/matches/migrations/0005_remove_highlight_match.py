# Generated by Django 4.2.13 on 2024-07-10 18:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0004_match_highlights_alter_highlight_match'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='highlight',
            name='match',
        ),
    ]
