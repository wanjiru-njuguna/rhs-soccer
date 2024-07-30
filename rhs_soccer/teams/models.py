import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _

from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField
from wagtail.models import Page
from wagtail.snippets.models import register_snippet



from rhs_soccer.payments.models import Campaign
from rhs_soccer.teams.enums import Season
from rhs_soccer.teams.enums import TeamLevel
from rhs_soccer.teams.managers import TeamManger
from rhs_soccer.users.enums import UserRoles
from rhs_soccer.users.models import User
from rhs_soccer.utils.common.singelton_page import SingletonPage



class TeamPage(SingletonPage):
    #title = models.CharField(max_length=255, verbose_name=_("Title"))
    subtitle = models.CharField(max_length=255, verbose_name=_("Subtitle"))
    description = RichTextField(verbose_name=_("Description"))
    content_panels = Page.content_panels + [
        FieldPanel('title'),
        FieldPanel('subtitle'),
        FieldPanel('description'),
    ]
    class Meta:
        verbose_name = _("Team Page")
        verbose_name_plural = _("Team Page")

    def __str__(self) -> str:
        return self.title

@register_snippet
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
    description = RichTextField(verbose_name=_("Team Description"))
    level = models.CharField(
        max_length=255,
        choices=TeamLevel.choices(),
        verbose_name=_("Team Level"),
        default=TeamLevel.VARSITY.value,
        blank=True,
        help_text=_("Team Level"),
    )
    image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True,
        null=True,
        verbose_name=_("Team Image")
    )
    fundraiser = models.ForeignKey(
        Campaign,
        on_delete=models.SET_NULL,
        related_name="campaigns",
        blank=True,
        null=True,
        limit_choices_to={"is_active": True},
    )
    objects = TeamManger()
    panels = [
        FieldPanel('uuid'),
        FieldPanel('home_team'),
        FieldPanel('name'),
        FieldPanel('short_name'),
        FieldPanel('head_coach'),
        FieldPanel('assistant_coach'),
        FieldPanel('season'),
        FieldPanel('description'),
        FieldPanel('level'),
        FieldPanel('image'),
        FieldPanel('fundraiser'),
    ]
    class Meta:
        verbose_name = _("Team")
        verbose_name_plural = _("Teams")

    def __str__(self):
        return self.name
