import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _

from rhs_soccer.payments.enums import DonationType
from rhs_soccer.users.models import User


class DonationPage(models.Model):
    title = models.CharField(max_length=255, verbose_name=_("Title"))
    subtitle = models.CharField(max_length=255, verbose_name=_("Subtitle"))
    image = models.ImageField(upload_to="donation_pages/", blank=True, null=True)
    description = models.TextField(_("description"), blank=True)

    class Meta:
        verbose_name = _("Donation Page")
        verbose_name_plural = _("Donation Pages")

    def __str__(self):
        return self.title


class Campaign(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(_("campaign name"), max_length=255)
    subtitle = models.CharField(max_length=255, verbose_name=_("Subtitle"))
    description = models.TextField(_("description"), blank=True)
    image = models.ImageField(upload_to="campaigns/", blank=True, null=True)
    goal = models.DecimalField(max_digits=10, decimal_places=2)
    raised = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    start_date = models.DateField()
    end_date = models.DateField()
    donations = models.ManyToManyField("Donation", related_name="campaign_donations", blank=True)
    is_active = models.BooleanField(default=False)

    class Meta:
        verbose_name = _("Campaign")
        verbose_name_plural = _("Campaigns")

    def __str__(self):
        return self.name




class Donation(models.Model):
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

    class Meta:
        verbose_name = _("Donation")
        verbose_name_plural = _("Donations")

    def __str__(self):
        return self.user.email


class PlayerFee(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="payments", limit_choices_to={"is_parent": True})
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    is_paid = models.BooleanField(default=False)

    class Meta:
        verbose_name = _("Payment")
        verbose_name_plural = _("Payments")

    def __str__(self):
        return self.user.email