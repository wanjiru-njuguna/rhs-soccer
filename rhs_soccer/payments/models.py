import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _

from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField
from wagtail.snippets.models import register_snippet
from modelcluster.models import ClusterableModel

from rhs_soccer.payments.enums import DonationType
from rhs_soccer.users.models import User


class DonationPage(Page):
    #title = models.CharField(max_length=255, verbose_name=_("Title"))
    subtitle = models.CharField(max_length=255, verbose_name=_("Subtitle"))
    image = models.ForeignKey(
        'wagtailimages.Image',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )
    description = models.TextField(_("description"), blank=True)
    content_panels = Page.content_panels + [
        FieldPanel('title'),
        FieldPanel('subtitle'),
        FieldPanel('image'),
        FieldPanel('description')


    ]
    class Meta:
        verbose_name = _("Donation Page")
        verbose_name_plural = _("Donation Pages")

    def __str__(self):
        return self.title

@register_snippet
class Campaign(ClusterableModel):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(_("campaign name"), max_length=255)
    subtitle = models.CharField(max_length=255, verbose_name=_("Subtitle"))
    description = models.TextField(_("description"), blank=True)
    image = models.ForeignKey(
        'wagtailimages.Image',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )
    goal = models.DecimalField(max_digits=10, decimal_places=2)
    raised = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    start_date = models.DateField()
    end_date = models.DateField()
    donations = models.ManyToManyField("Donation", related_name="campaign_donations", blank=True)
    is_active = models.BooleanField(default=False)

    panels = [
        FieldPanel('uuid'),
        FieldPanel('name'),
        FieldPanel('subtitle'),
        FieldPanel('description'),
        FieldPanel('image'),
        FieldPanel('goal'),
        FieldPanel('raised'),
        FieldPanel('start_date'),
        FieldPanel('end_date'),
        FieldPanel('donations'),
        FieldPanel('is_active'),

    ]

    class Meta:
        verbose_name = _("Campaign")
        verbose_name_plural = _("Campaigns")

    def __str__(self):
        return self.name



@register_snippet
class Donation(ClusterableModel):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="donations")
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE, related_name="campaign_donation", blank=True, null=True)
    donation_type = models.CharField(
        max_length=255,
        choices=DonationType.choices(),
        default=DonationType.ONE_TIME.name,
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    panels = [
        FieldPanel('uuid'),
        FieldPanel('user'),
        FieldPanel('campaign'),
        FieldPanel('donation_type'),
        FieldPanel('amount'),
        FieldPanel('date'),

    ]
    class Meta:
        verbose_name = _("Donation")
        verbose_name_plural = _("Donations")

    def __str__(self):
        return self.user.email

@register_snippet
class PlayerFee(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="payments", limit_choices_to={"is_parent": True})
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    is_paid = models.BooleanField(default=False)
    panels = [
        FieldPanel('uuid'),
        FieldPanel('user'),
        FieldPanel('amount'),
        FieldPanel('date'),
        FieldPanel('is_paid'),

    ]
    class Meta:
        verbose_name = _("Payment")
        verbose_name_plural = _("Payments")

    def __str__(self):
        return self.user.email