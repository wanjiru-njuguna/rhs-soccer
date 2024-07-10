# Generated by Django 4.2.13 on 2024-07-10 00:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields
import tinymce.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True, verbose_name='uuid')),
                ('title', models.CharField(max_length=200, verbose_name='event title')),
                ('slug', models.SlugField(max_length=200, unique=True, verbose_name='slug')),
                ('event_type', models.CharField(choices=[('game', 'Game'), ('practice', 'Practice'), ('tournament', 'Tournament'), ('meeting', 'Meeting'), ('banquet', 'Banquet'), ('award', 'Award'), ('other', 'Other')], default='game', max_length=220, verbose_name='event type')),
                ('description', tinymce.models.HTMLField(blank=True, verbose_name='event description')),
                ('image', models.ImageField(blank=True, upload_to='events/', verbose_name='image')),
                ('start_date', models.DateTimeField(verbose_name='start date')),
                ('end_date', models.DateTimeField(blank=True, null=True, verbose_name='end date')),
                ('is_paid', models.BooleanField(default=False, verbose_name='is paid')),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='price')),
                ('need_volunteers', models.BooleanField(default=False, verbose_name='need volunteers')),
                ('volunteers_needed', models.PositiveIntegerField(default=0, verbose_name='volunteers needed')),
                ('volunteer_credits', models.PositiveIntegerField(default=0, verbose_name='volunteer credits')),
                ('is_published', models.BooleanField(default=False, verbose_name='is published')),
            ],
            options={
                'verbose_name': 'event',
                'verbose_name_plural': 'events',
            },
        ),
        migrations.CreateModel(
            name='EventPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='title')),
                ('slug', models.SlugField(max_length=200, unique=True, verbose_name='slug')),
                ('content', tinymce.models.HTMLField(blank=True, verbose_name='content')),
            ],
            options={
                'verbose_name': 'event page',
                'verbose_name_plural': 'event pages',
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True, verbose_name='uuid')),
                ('name', models.CharField(max_length=200, verbose_name='location name')),
                ('slug', models.SlugField(max_length=200, unique=True, verbose_name='slug')),
                ('address', models.CharField(blank=True, max_length=200, verbose_name='address')),
                ('city', models.CharField(blank=True, max_length=200, verbose_name='city')),
                ('state', models.CharField(blank=True, choices=[('Alabama', 'Alabama'), ('Alaska', 'Alaska'), ('Arizona', 'Arizona'), ('Arkansas', 'Arkansas'), ('California', 'California'), ('Colorado', 'Colorado'), ('Connecticut', 'Connecticut'), ('Delaware', 'Delaware'), ('Florida', 'Florida'), ('Georgia', 'Georgia'), ('Hawaii', 'Hawaii'), ('Idaho', 'Idaho'), ('Illinois', 'Illinois'), ('Indiana', 'Indiana'), ('Iowa', 'Iowa'), ('Kansas', 'Kansas'), ('Kentucky', 'Kentucky'), ('Louisiana', 'Louisiana'), ('Maine', 'Maine'), ('Maryland', 'Maryland'), ('Massachusetts', 'Massachusetts'), ('Michigan', 'Michigan'), ('Minnesota', 'Minnesota'), ('Mississippi', 'Mississippi'), ('Missouri', 'Missouri'), ('Montana', 'Montana'), ('Nebraska', 'Nebraska'), ('Nevada', 'Nevada'), ('New Hampshire', 'New Hampshire'), ('New Jersey', 'New Jersey'), ('New Mexico', 'New Mexico'), ('New York', 'New York'), ('North Carolina', 'North Carolina'), ('North Dakota', 'North Dakota'), ('Ohio', 'Ohio'), ('Oklahoma', 'Oklahoma'), ('Oregon', 'Oregon'), ('Pennsylvania', 'Pennsylvania'), ('Rhode Island', 'Rhode Island'), ('South Carolina', 'South Carolina'), ('South Dakota', 'South Dakota'), ('Tennessee', 'Tennessee'), ('Texas', 'Texas'), ('Utah', 'Utah'), ('Vermont', 'Vermont'), ('Virginia', 'Virginia'), ('Washington', 'Washington'), ('West Virginia', 'West Virginia'), ('Wisconsin', 'Wisconsin'), ('Wyoming', 'Wyoming')], default='Minnesota', max_length=200, verbose_name='state')),
                ('zip_code', models.CharField(blank=True, max_length=10, verbose_name='zip code')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=20, region=None, verbose_name='phone')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email')),
                ('website', models.URLField(blank=True, verbose_name='website')),
                ('description', tinymce.models.HTMLField(blank=True, verbose_name='description')),
            ],
            options={
                'verbose_name': 'location',
                'verbose_name_plural': 'locations',
            },
        ),
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True, verbose_name='uuid')),
                ('credits', models.PositiveIntegerField(default=0, verbose_name='credits')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='volunteers', to='events.event', verbose_name='event')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events_volunteering', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'volunteer',
                'verbose_name_plural': 'volunteers',
            },
        ),
        migrations.AddField(
            model_name='event',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.location', verbose_name='location'),
        ),
        migrations.AddField(
            model_name='event',
            name='organizer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='organized_events', to=settings.AUTH_USER_MODEL, verbose_name='organizer'),
        ),
        migrations.CreateModel(
            name='Attendee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True, verbose_name='uuid')),
                ('guests', models.PositiveIntegerField(default=0, verbose_name='guests')),
                ('is_paid', models.BooleanField(default=False, verbose_name='is paid')),
                ('paid_date', models.DateTimeField(blank=True, null=True, verbose_name='paid date')),
                ('paid_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='paid amount')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attendees', to='events.event', verbose_name='event')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events_attending', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'attendee',
                'verbose_name_plural': 'attendees',
            },
        ),
    ]
