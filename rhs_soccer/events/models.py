import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
from phonenumber_field.modelfields import PhoneNumberField
from solo.models import SingletonModel
from tinymce.models import HTMLField

from rhs_soccer.events.enums import EvenType
from rhs_soccer.events.managers import AttendeeManager
from rhs_soccer.events.managers import EventManager
from rhs_soccer.events.managers import VolunteerManager
from rhs_soccer.users.models import User
from rhs_soccer.utils.common.enums import UsStates


class EventPage(SingletonModel):
    title = models.CharField(_("title"), max_length=200)
    content = HTMLField(_("content"), blank=True)

    class Meta:
        verbose_name = _("event page")
        verbose_name_plural = _("event pages")

    def __str__(self):
        return self.title


class Location(models.Model):
    uuid = models.UUIDField(_("uuid"), default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(_("location name"), max_length=200)
    slug = models.SlugField(_("slug"), max_length=200, unique=True, editable=False)
    address = models.CharField(_("address"), max_length=200, blank=True)
    city = models.CharField(_("city"), max_length=200, blank=True)
    state = models.CharField(
        _("state"),
        max_length=200,
        blank=True,
        choices=UsStates.choices(),
        default=UsStates.MINNESOTA.value,
    )
    zip_code = models.CharField(_("zip code"), max_length=10, blank=True)
    phone = PhoneNumberField(_("phone"), max_length=20, blank=True)
    email = models.EmailField(_("email"), blank=True)
    website = models.URLField(_("website"), blank=True)
    description = HTMLField(_("description"), blank=True)

    class Meta:
        verbose_name = _("location")
        verbose_name_plural = _("locations")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class Event(models.Model):
    uuid = models.UUIDField(_("uuid"), default=uuid.uuid4, editable=False, unique=True)
    organizer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name=_("organizer"),
        related_name="organized_events",
    )
    title = models.CharField(_("event title"), max_length=200)
    slug = models.SlugField(_("slug"), max_length=200, unique=True, editable=False)
    event_type = models.CharField(
        _("event type"),
        max_length=220,
        choices=EvenType.choices(),
        default=EvenType.GAME.value,
    )
    description = HTMLField(_("event description"), blank=True)
    image = models.ImageField(_("image"), upload_to="events/", blank=True)
    start_date = models.DateTimeField(_("start date"))
    end_date = models.DateTimeField(_("end date"), blank=True, null=True)
    location = models.ForeignKey(
        Location,
        on_delete=models.CASCADE,
        verbose_name=_("location"),
    )
    is_paid = models.BooleanField(_("is paid"), default=False)
    price = models.DecimalField(
        _("price"),
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True,
    )
    need_volunteers = models.BooleanField(_("need volunteers"), default=False)
    volunteers_needed = models.PositiveIntegerField(_("volunteers needed"), default=0)
    volunteer_credits = models.PositiveIntegerField(_("volunteer credits"), default=0)
    is_published = models.BooleanField(_("is published"), default=False)

    objects = EventManager()

    class Meta:
        verbose_name = _("event")
        verbose_name_plural = _("events")

    def __str__(self):
        return self.title
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Attendee(models.Model):
    uuid = models.UUIDField(_("uuid"), default=uuid.uuid4, editable=False, unique=True)
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        verbose_name=_("event"),
        related_name="attendees",
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name=_("user"),
        related_name="events_attending",
    )
    guests = models.PositiveIntegerField(_("guests"), default=0)
    is_paid = models.BooleanField(_("is paid"), default=False)
    paid_date = models.DateTimeField(_("paid date"), blank=True, null=True)
    paid_amount = models.DecimalField(
        _("paid amount"),
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True,
    )

    objects = AttendeeManager()

    class Meta:
        verbose_name = _("attendee")
        verbose_name_plural = _("attendees")

    def __str__(self):
        return f"{self.user} - {self.event}"


class Volunteer(models.Model):
    uuid = models.UUIDField(_("uuid"), default=uuid.uuid4, editable=False, unique=True)
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        verbose_name=_("event"),
        related_name="volunteers",
        limit_choices_to={"need_volunteers": True},
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name=_("user"),
        related_name="events_volunteering",
    )
    credits = models.PositiveIntegerField(_("credits"), default=0)

    objects = VolunteerManager()

    class Meta:
        verbose_name = _("volunteer")
        verbose_name_plural = _("volunteers")

    def __str__(self):
        return f"{self.user} - {self.event}"
