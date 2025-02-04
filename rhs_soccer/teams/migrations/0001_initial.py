# Generated by Django 4.2.13 on 2024-08-01 10:57

from django.db import migrations, models
import django.db.models.deletion
import uuid
import wagtail.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0093_uploadedfile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('home_team', models.BooleanField(default=True, verbose_name='Home Team')),
                ('name', models.CharField(max_length=255, verbose_name='Team Name')),
                ('short_name', models.CharField(blank=True, max_length=255, verbose_name='Team Short Name')),
                ('season', models.CharField(blank=True, choices=[('2024-2025', '2024-2025'), ('2025-2026', '2025-2026'), ('2026-2027', '2026-2027'), ('2027-2028', '2027-2028'), ('2028-2029', '2028-2029')], default='2024-2025', help_text='Season', max_length=255, verbose_name='Season')),
                ('description', wagtail.fields.RichTextField(verbose_name='Team Description')),
                ('level', models.CharField(blank=True, choices=[('Varsity', 'Varsity'), ('JV', 'JV'), ('Sophmore', 'Sophmore'), ('Freshman', 'Freshman')], default='Varsity', help_text='Team Level', max_length=255, verbose_name='Team Level')),
            ],
            options={
                'verbose_name': 'Team',
                'verbose_name_plural': 'Teams',
            },
        ),
        migrations.CreateModel(
            name='TeamPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('subtitle', models.CharField(max_length=255, verbose_name='Subtitle')),
                ('description', wagtail.fields.RichTextField(verbose_name='Description')),
            ],
            options={
                'verbose_name': 'Team Page',
                'verbose_name_plural': 'Team Page',
            },
            bases=('wagtailcore.page', models.Model),
        ),
    ]
