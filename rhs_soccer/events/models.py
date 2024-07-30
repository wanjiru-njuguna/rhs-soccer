import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
from phonenumber_field.modelfields import PhoneNumberField
from solo.models import SingletonModel

from wagtail.models import Page, PageManager
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.fields import RichTextField
from wagtail.snippets.models import register_snippet
from modelcluster.models import ClusterableModel

from rhs_soccer.events.enums import EvenType
from rhs_soccer.events.managers import AttendeeManager
from rhs_soccer.events.managers import EventManager
from rhs_soccer.events.managers import VolunteerManager
from rhs_soccer.users.models import User
from rhs_soccer.utils.common.enums import UsStates
from rhs_soccer.utils.common.singelton_page import SingletonPage



class EventPage(SingletonModel):
    title = models.CharField(_("title"), max_length=200)
    content = RichTextField(_("content"), blank=True)

    class Meta:
        verbose_name = _("event page")
        verbose_name_plural = _("event pages")

    def __str__(self):
        return self.title

@register_snippet
class Location(ClusterableModel):
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
    description = RichTextField(_("description"), blank=True)
    panels = [
        FieldPanel('uuid'),
        FieldPanel('name'),
        FieldPanel('slug'),
        FieldPanel('address'),
        FieldPanel('city'),
        FieldPanel('state'),
        FieldPanel('zip_code'),
        FieldPanel('phone'),
        FieldPanel('email'),
        FieldPanel('website'),
        FieldPanel('description'),

    ]
    class Meta:
        verbose_name = _("location")
        verbose_name_plural = _("locations")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class EventPageManager(PageManager):
    pass
class Event(Page):
    uuid = models.UUIDField(_("uuid"), default=uuid.uuid4, editable=False, unique=True)
    organizer = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        verbose_name=_("organizer"),
        related_name="organized_events",
        null = True,
    )
    name = models.CharField(_("event name"), max_length=200, default = 'Soccer_match')
    slug_field = models.SlugField(_("slug_field"), max_length=200, unique=True, editable=False)
    event_type = models.CharField(
        _("event type"),
        max_length=220,
        choices=EvenType.choices(),
        default=EvenType.GAME.value,
    )
    description = RichTextField(_("event description"), blank=True)
    image = models.ForeignKey('wagtailimages.Image',on_delete=models.SET_NULL, null = True, blank=True)
    start_date = models.DateTimeField(_("start date"))
    end_date = models.DateTimeField(_("end date"), blank=True, null=True)
    location = models.ForeignKey(
        Location,
        on_delete=models.SET_NULL,
        verbose_name=_("location"),
        null = True,
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
    
    objects = EventPageManager()

    content_panels = Page.content_panels + [
        FieldPanel('organizer'),
        FieldPanel('name'),
        # FieldPanel('slug_field'),
        FieldPanel('event_type'),
        FieldPanel('description'),
        FieldPanel('image'),
        FieldPanel('start_date'),
        FieldPanel('end_date'),
        FieldPanel('location'),
        FieldPanel('is_paid'),
        FieldPanel('price'),
        FieldPanel('need_volunteers'),
        FieldPanel('volunteers_needed'),
        FieldPanel('volunteer_credits'),
        FieldPanel('is_published'),

    ]
    class Meta:
        verbose_name = _("event")
        verbose_name_plural = _("events")

    def __str__(self):
        return self.title
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

@register_snippet
class Attendee(ClusterableModel):
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
    panels = [
        FieldPanel('event'),
        FieldPanel('user'),
         FieldPanel('guests'),
        FieldPanel('is_paid'),
        FieldPanel('paid_date'),
        FieldPanel('paid_amount'),
        FieldPanel('objects'),

    ]
    class Meta:
        verbose_name = _("attendee")
        verbose_name_plural = _("attendees")

    def __str__(self):
        return f"{self.user} - {self.event}"

@register_snippet
class Volunteer(ClusterableModel):
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
    panels = [
        FieldPanel('event'),
        FieldPanel('user'),
        FieldPanel('credits'),
        FieldPanel('objects'),

    ]
    class Meta:
        verbose_name = _("volunteer")
        verbose_name_plural = _("volunteers")

    def __str__(self):
        return f"{self.user} - {self.event}"
