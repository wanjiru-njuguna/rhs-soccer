# Generated by Django 4.2.13 on 2024-07-10 01:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='campaign',
            name='is_published',
        ),
    ]
