import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from tinymce.models import HTMLField
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.fields import RichTextField
from wagtail.snippets.models import register_snippet
from modelcluster.models import ClusterableModel


from rhs_soccer.profiles.enums import EmergencyContactRelationship
from rhs_soccer.profiles.enums import PlayerGrade
from rhs_soccer.profiles.enums import PlayerPosition
from rhs_soccer.profiles.enums import PlayerStatus
from rhs_soccer.teams.models import Team
from rhs_soccer.users.enums import UserRoles
from rhs_soccer.users.models import User
from rhs_soccer.utils.common.enums import UsStates


class Profile(Page):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, related_name="profile", null = True)
    phone = PhoneNumberField(_("Phone"), max_length=255, blank=True)
    avatar = models.ForeignKey('wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name=_("Avatar"))
    
    content_panels = Page.content_panels + [
        FieldPanel('user'),
        FieldPanel('phone'),
        FieldPanel('avatar'),
    ]
    class Meta:
        verbose_name = _("Profile")
        verbose_name_plural = _("Profiles")

    def __str__(self):
        return self.user.get_full_name()

@register_snippet
class Address(models.Model):
    address = models.CharField(max_length=255, verbose_name=_("Address"))
    address2 = models.CharField(
        max_length=255,
        verbose_name=_("Address 2"),
        blank=True,
    )
    city = models.CharField(max_length=255, verbose_name=_("City"))
    state = models.CharField(
        max_length=255,
        verbose_name=_("State"),
        choices=UsStates.choices(),
        default=UsStates.MINNESOTA.value,
    )
    zip_code = models.CharField(max_length=255, verbose_name=_("Zip Code"))
    panels = [
        FieldPanel('address'),
        FieldPanel('address2'),
        FieldPanel('city'),
        FieldPanel('state'),
        FieldPanel('zip_code'),

    ]
    class Meta:
        verbose_name = _("Address")
        verbose_name_plural = _("Addresses")

    def __str__(self) -> str:
        return self.address

@register_snippet
class Player(ClusterableModel):
    uuid = models.UUIDField(_("UUID"), default=uuid.uuid4, editable=False, unique=True)
    team = models.ForeignKey(
        Team,
        on_delete=models.SET_NULL,
        related_name="players",
        blank=True,
        null=True,
    )
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name="player")
    jeresy_number = models.CharField(_("Jeresy Number"), blank=True, max_length=10)
    grade = models.CharField(
        _("Grade"),
        choices=PlayerGrade.choices(),
        blank=True,
        help_text=_("Grade"),
        max_length=2,
    )
    position = models.CharField(
        _("Position"),
        max_length=255,
        blank=True,
        choices=PlayerPosition.choices(),
    )
    height = models.CharField(
        _("Height"),
        max_length=255,
        blank=True,
    )
    weight = models.CharField(
        _("Weight"),
        max_length=255,
        blank=True,
    )
    status = models.CharField(
        max_length=255,
        choices=PlayerStatus.choices(),
        verbose_name=_("Status"),
        blank=True,
        help_text=_("Status"),
    )
    bio = RichTextField(
        _("Bio"),
        blank=True,
    )
    is_published = models.BooleanField(_("Published"), default=False)
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)
    panels = [
        FieldPanel('uuid'),
        FieldPanel('team'),
        FieldPanel('profile'),
        FieldPanel('jersey_number'),
        FieldPanel('grade'),
        FieldPanel('position'),
        FieldPanel('height'),
        FieldPanel('weight'),
        FieldPanel('status'),
        FieldPanel('bio'),
        FieldPanel('is_published'),
    ]
    class Meta:
        verbose_name = _("Player")
        verbose_name_plural = _("Players")

    def __str__(self):
        return self.profile.user.get_full_name()

    def get_avatar(self):
        return self.profile.avatar

    get_avatar.short_description = _("Avatar")

    def get_short_name(self):
        return self.profile.user.get_short_name()

@register_snippet
class Parent(ClusterableModel):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name="parent")
    players = models.ManyToManyField(Player, related_name="parents", blank=True)
    address = models.ForeignKey(
        Address,
        on_delete=models.SET_NULL,
        related_name="parents",
        blank=True,
        null=True,
    )
    emergency_contact_name = models.CharField(
        _("Emergency Contact Name"),
        max_length=50,
        blank=True,
    )
    emergency_contact_phone = PhoneNumberField(
        _("Emergency Contact Phone"),
        max_length=20,
        blank=True,
    )
    emergency_contact_relationship = models.CharField(
        _("Emergency Contact Relationship"),
        max_length=50,
        blank=True,
        choices=EmergencyContactRelationship.choices(),
        default=EmergencyContactRelationship.OTHER.value,
    )
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)
    panels = [
        FieldPanel('profile'),
        FieldPanel('players'),
        FieldPanel('address'),
        FieldPanel('emergency_contact_name'),
        FieldPanel('emergency_contact_phone'),
        FieldPanel('emergency_contact_relationship'),
        FieldPanel('created_at'),
        FieldPanel('updated_at'),
    ]

    class Meta:
        verbose_name = _("Parent")
        verbose_name_plural = _("Parents")

    def __str__(self):
        return self.profile.get_full_name()

    def get_full_name(self):
        return self.profile.get_full_name()

    get_full_name.short_description = _("Full Name")

@register_snippet
class Coach(models.Model):
    uuid = models.UUIDField(_("UUID"), default=uuid.uuid4, editable=False, unique=True)
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name="coach")
    address = models.ForeignKey(
        Address,
        on_delete=models.SET_NULL,
        related_name="coaches",
        blank=True,
        null=True,
    )
    bio = RichTextField(_("Bio"), blank=True)
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)
    panels = [
        FieldPanel('uuid'),
        FieldPanel('profile'),
        FieldPanel('address'),
        FieldPanel('bio'),
        FieldPanel('created_at'),
        FieldPanel('updated_at'),
    ]
    class Meta:
        verbose_name = _("Coach")
        verbose_name_plural = _("Coaches")

    def __str__(self):
        return self.profile.get_full_name()

    def get_full_name(self):
        return self.profile.get_full_name()

    get_full_name.short_description = _("Full Name")

@register_snippet
class Manager(models.Model):
    uuid = models.UUIDField(_("UUID"), default=uuid.uuid4, editable=False, unique=True)
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name="manager")
    address = models.ForeignKey(
        Address,
        on_delete=models.SET_NULL,
        related_name="managers",
        blank=True,
        null=True,
    )
    bio = RichTextField(_("Bio"), blank=True)
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)
    panels = [
        FieldPanel('uuid'),
        FieldPanel('profile'),
        FieldPanel('address'),
        FieldPanel('bio'),
        FieldPanel('created_at'),
        FieldPanel('updated_at'),


    ]
    class Meta:
        verbose_name = _("Manager")
        verbose_name_plural = _("Managers")

    def __str__(self):
        return self.user.get_full_name()

    def get_full_name(self):
        return self.user.get_full_name()

    get_full_name.short_description = _("Full Name")
