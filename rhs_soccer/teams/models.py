import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _
from solo.models import SingletonModel
from tinymce.models import HTMLField

from rhs_soccer.payments.models import Campaign
from rhs_soccer.teams.enums import Season
from rhs_soccer.teams.enums import TeamLevel
from rhs_soccer.teams.managers import TeamManger
from rhs_soccer.users.enums import UserRoles
from rhs_soccer.users.models import User


class TeamPage(SingletonModel):
    title = models.CharField(max_length=255, verbose_name=_("Title"))
    subtitle = models.CharField(max_length=255, verbose_name=_("Subtitle"))
    description = HTMLField(verbose_name=_("Description"))

    class Meta:
        verbose_name = _("Team Page")
        verbose_name_plural = _("Team Page")

    def __str__(self) -> str:
        return self.title


class Team(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    home_team = models.BooleanField(_("Home Team"), default=True)
    name = models.CharField(max_length=255, verbose_name=_("Team Name"))
    short_name = models.CharField(
        max_length=255,
        verbose_name=_("Team Short Name"),
        blank=True,
    )
    head_coach = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name="head_coach",
        blank=True, null=True,
        verbose_name=_("Head Coach"),
        limit_choices_to={"role": UserRoles.COACH.value},
    )
    assistant_coach = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name="assistant_coach",
        blank=True, null=True,
        verbose_name=_("Assistant Coach"),
        limit_choices_to={"role": UserRoles.COACH.value},
    )
    season = models.CharField(
        max_length=255,
        verbose_name=_("Season"),
        choices=Season.choices(),
        default=Season.SEASON1.value,
        blank=True,
        help_text=_("Season"),
    )
    description = HTMLField(verbose_name=_("Team Description"))
    level = models.CharField(
        max_length=255,
        choices=TeamLevel.choices(),
        verbose_name=_("Team Level"),
        default=TeamLevel.VARSITY.value,
        blank=True,
        help_text=_("Team Level"),
    )
    image = models.ImageField(upload_to="teams", verbose_name=_("Team Image"), blank=True)
    fundraiser = models.ForeignKey(
        Campaign,
        on_delete=models.SET_NULL,
        related_name="campaigns",
        blank=True,
        null=True,
        limit_choices_to={"is_active": True},
    )
    objects = TeamManger()

    class Meta:
        verbose_name = _("Team")
        verbose_name_plural = _("Teams")

    def __str__(self):
        return self.name
