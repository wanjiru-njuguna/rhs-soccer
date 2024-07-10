import uuid

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from tinymce.models import HTMLField

from rhs_soccer.matches.managers import MatchManager
from rhs_soccer.teams.models import Team
from rhs_soccer.matches.enums import MatchHighlight
from rhs_soccer.utils.common.enums import UsStates


class Venue(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=255, verbose_name=_("Name"))
    address = models.CharField(max_length=255, verbose_name=_("Address"))
    city = models.CharField(max_length=255, verbose_name=_("City"))
    state = models.CharField(
        max_length=20,
        choices=UsStates.choices(),
        default=UsStates.MINNESOTA.value,
        verbose_name=_("State"),
    )
    zip_code = models.CharField(max_length=10, verbose_name=_("Zip Code"))
    phone = PhoneNumberField(verbose_name=_("Phone"))
    email = models.EmailField(verbose_name=_("Email"))
    website = models.URLField(verbose_name=_("Website"))
    description = HTMLField(verbose_name=_("Description"))

    class Meta:
        verbose_name = _("Venue")
        verbose_name_plural = _("Venues")

    def __str__(self) -> str:
        return self.name


class Match(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    home_team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE,
        verbose_name=_("Home Team"),
        related_name="home_team_matches",
        blank=True,
        null=True,
        limit_choices_to={"home_team": True},
    )
    away_team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE,
        verbose_name=_("Away Team"),
        related_name="away_team_matches",
        blank=True,
        null=True,
        limit_choices_to={"home_team": False},
    )
    venue = models.ForeignKey(
        Venue,
        on_delete=models.CASCADE,
        verbose_name=_("Venue"),
        related_name="venue",
    )
    date = models.DateField(verbose_name=_("Date"))
    time = models.TimeField(verbose_name=_("Time"))
    regulation_time = models.PositiveIntegerField(
        verbose_name=_("Regulation Time"),
        default=90,
        help_text=_("In minutes"),
        validators=[MinValueValidator(1), MaxValueValidator(120)],
    )
    is_overtime = models.BooleanField(
        verbose_name=_("Overtime"),
        default=False,
    )
    is_postponed = models.BooleanField(
        verbose_name=_("Postponed"),
        default=False,
    )
    is_canceled = models.BooleanField(
        verbose_name=_("Canceled"),
        default=False,
    )
    is_penalty_shootout = models.BooleanField(
        verbose_name=_("Penalty Shootout"),
        default=False,
    )
    home_team_score = models.PositiveIntegerField(
        verbose_name=_("Home Team Score"),
        default=0,
    )
    away_team_score = models.PositiveIntegerField(
        verbose_name=_("Away Team Score"),
        default=0,
    )
    summary = models.TextField(verbose_name=_("Summary"), blank=True)
    highlights = models.ManyToManyField(
        "Highlight",
        verbose_name=_("Highlights"),
        related_name="matche_highlights",
        blank=True,
    )
    is_active = models.BooleanField(verbose_name=_("Is Active"), default=True)

    objects = MatchManager()

    class Meta:
        verbose_name = _("Match")
        verbose_name_plural = _("Matches")

    def __str__(self) -> str:
        return f"{self.home_team.short_name} vs {self.away_team.short_name}"

    @property
    def is_upcoming(self):
        return self.date >= timezone.now().date() and self.is_active

    @property
    def is_past(self):
        return self.date < timezone.now().date() and self.is_active

    @property
    def is_today(self):
        return self.date == timezone.now().date() and self.is_active


class Highlight(models.Model):
    highlight = models.CharField(
        max_length=50,
        choices=MatchHighlight.choices(),
        default=MatchHighlight.GOAL.value,
        verbose_name=_("Highlight"),
        blank=True,
    )
    player = models.ForeignKey(
        "profiles.Player",
        on_delete=models.CASCADE,
        verbose_name=_("Player"),
        related_name="highlights",
        blank=True,
    )

    class Meta:
        verbose_name = _("Match Highlight")
        verbose_name_plural = _("Match Highlights")

    def __str__(self) -> str:
        return f"{self.match} - {self.highlight} - {self.player}"
