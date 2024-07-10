import uuid
from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from solo.models import SingletonModel
from tinymce.models import HTMLField

from rhs_soccer.core.enums import DificultyLevel
from rhs_soccer.core.enums import OfficerPosition
from rhs_soccer.core.enums import SponsorshipLevel
from rhs_soccer.utils.common import file_cleanup
from rhs_soccer.utils.common.enums import UsStates
from rhs_soccer.utils.helpers.models import TimeStamp


class Address(SingletonModel):
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
    )
    zip_code = models.CharField(max_length=255, verbose_name=_("Zip Code"))

    class Meta:
        verbose_name = _("Address")
        verbose_name_plural = _("Addresses")

    def __str__(self) -> str:
        return self.address


class SiteSettings(SingletonModel):
    name = models.CharField(max_length=255, verbose_name=_("Name"))
    short_name = models.CharField(max_length=50, verbose_name=_("Short Name"))
    tagline = models.CharField(max_length=255, verbose_name=_("Tagline"), blank=True)
    logo = models.ImageField(
        upload_to="site_assets",
        verbose_name=_("Logo"),
        blank=True,
        null=True,
    )
    dark_logo = models.ImageField(
        upload_to="site_assets",
        verbose_name=_("Dark Logo"),
        blank=True,
        null=True,
    )
    favicon = models.ImageField(
        upload_to="site_assets",
        verbose_name=_("Favicon"),
        blank=True,
        null=True,
    )
    phone = PhoneNumberField(max_length=255, verbose_name=_("Phone"))
    email = models.CharField(max_length=255, verbose_name=_("Email"))
    address = models.ForeignKey(
        Address,
        on_delete=models.SET_NULL,
        related_name="site_address",
        blank=True,
        null=True,
    )
    social_media = models.OneToOneField(
        "SocialMedia",
        blank=True,
        null=True,
        verbose_name=_("Social Media"),
        on_delete=models.SET_NULL,
        related_name="social_media",
    )
    description = models.TextField(verbose_name=_("Description"), blank=True)
    keywords = models.TextField(verbose_name=_("Keywords"), blank=True)
    fund_raising_mode = models.BooleanField(_("Fund Raising Mode"), default=False)

    class Meta:
        verbose_name = _("Site Settings")
        verbose_name_plural = _("Site Settings")

    def __str__(self):
        return self.name

file_cleanup.delete_file_on_model_delete(SiteSettings, "logo")
file_cleanup.delete_file_on_model_delete(SiteSettings, "favicon")
file_cleanup.delete_file_on_model_delete(SiteSettings, "dark_logo")


class SocialMedia(SingletonModel):
    site = models.ForeignKey(
        "SiteSettings",
        on_delete=models.CASCADE,
        verbose_name=_("Site"),
        related_name="social_media_site",
    )
    faecbook = models.URLField(verbose_name=_("Facebook URL"), blank=True)
    twitter = models.URLField(verbose_name=_("Twitter URL"), blank=True)
    instagram = models.URLField(verbose_name=_("Instagram URL"), blank=True)
    linkedin = models.URLField(verbose_name=_("LinkedIn URL"), blank=True)
    youtube = models.URLField(verbose_name=_("YouTube URL"), blank=True)

    class Meta:
        verbose_name = _("Social Media")
        verbose_name_plural = _("Social Media")

    def __str__(self):
        return f"{self.site.name} Social Media"


class AboutPage(TimeStamp, SingletonModel):
    title = models.CharField(max_length=255, verbose_name=_("Title"))
    subtitle = models.CharField(max_length=255, verbose_name=_("Subtitle"), blank=True)
    content = HTMLField(verbose_name=_("Content"))
    image = models.ImageField(
        upload_to="pages",
        verbose_name=_("Image"),
        blank=True,
        null=True,
        help_text=_("Image size should be 1920 x 1080"),
    )

    class Meta:
        verbose_name = _("About Page")
        verbose_name_plural = _("About Page")

    def __str__(self) -> str:
        return self.title

file_cleanup.delete_file_on_model_delete(AboutPage, "image")


class ContactPage(TimeStamp, SingletonModel):
    title = models.CharField(max_length=255, verbose_name=_("Title"))
    subtitle = models.CharField(max_length=255, verbose_name=_("Subtitle"))
    image = models.ImageField(
        upload_to="pages",
        verbose_name=_("Image"),
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = _("Contact Page")
        verbose_name_plural = _("Contact Page")

    def __str__(self) -> str:
        return self.title

file_cleanup.delete_file_on_model_delete(ContactPage, "image")


class Contact(TimeStamp):
    first_name = models.CharField(max_length=255, verbose_name=_("First Name"))
    last_name = models.CharField(max_length=255, verbose_name=_("Last Name"))
    email = models.EmailField(verbose_name=_("Email"))
    phone = PhoneNumberField(verbose_name=_("Phone"), blank=True)
    message = models.TextField(verbose_name=_("Message"))

    class Meta:
        verbose_name = _("Contact")
        verbose_name_plural = _("Contacts")

    def __str__(self) -> str:
        return self.email


class PrivacyPolicyPage(TimeStamp, SingletonModel):
    title = models.CharField(max_length=255, verbose_name=_("Title"))
    subtitle = models.CharField(max_length=255, verbose_name=_("Subtitle"), blank=True)
    content = HTMLField(verbose_name=_("Content"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created At"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Updated At"))

    class Meta:
        verbose_name = _("Privacy Policy Page")
        verbose_name_plural = _("Privacy Policy Page")

    def __str__(self) -> str:
        return self.title


class TermsOfServicePage(TimeStamp, SingletonModel):
    title = models.CharField(max_length=255, verbose_name=_("Title"))
    subtitle = models.CharField(max_length=255, verbose_name=_("Subtitle"), blank=True)
    content = HTMLField(verbose_name=_("Content"))

    class Meta:
        verbose_name = _("Terms of Service Page")
        verbose_name_plural = _("Terms of Service Page")

    def __str__(self) -> str:
        return self.title


class BoosterPage(SingletonModel):
    title = models.CharField(max_length=255, verbose_name=_("Title"))
    subtitle = models.CharField(max_length=255, verbose_name=_("Subtitle"), blank=True)
    heading = models.CharField(max_length=255, verbose_name=_("Heading"))
    content = HTMLField(verbose_name=_("Content"))
    image = models.ImageField(
        upload_to="pages",
        verbose_name=_("Image"),
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = _("Booster Page")
        verbose_name_plural = _("Booster Page")

    def __str__(self) -> str:
        return self.title

file_cleanup.delete_file_on_model_delete(BoosterPage, "image")


class BoosterOfficer(models.Model):
    first_name = models.CharField(max_length=255, verbose_name=_("First Name"))
    last_name = models.CharField(max_length=255, verbose_name=_("Last Name"))
    title = models.CharField(
        max_length=255,
        verbose_name=_("Title"),
        choices=OfficerPosition.choices(),
        blank=True)
    email = models.EmailField(verbose_name=_("Email"))
    phone = models.CharField(max_length=255, verbose_name=_("Phone"))
    image = models.ImageField(
        upload_to="pages",
        verbose_name=_("Image"),
        blank=True,
        null=True,
    )
    bio = HTMLField(verbose_name=_("Bio"), blank=True)

    class Meta:
        verbose_name = _("Booster Officer")
        verbose_name_plural = _("Booster Officers")

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

file_cleanup.delete_file_on_model_delete(BoosterOfficer, "image")


class SponsorPage(SingletonModel):
    title = models.CharField(max_length=255, verbose_name=_("Title"))
    subtitle = models.CharField(max_length=255, verbose_name=_("Subtitle"), blank=True)
    heading = models.CharField(max_length=255, verbose_name=_("Heading"))
    content = HTMLField(verbose_name=_("Content"))
    cta = models.CharField(max_length=255, verbose_name=_("Call to Action"))
    image = models.ImageField(
        upload_to="pages",
        verbose_name=_("Image"),
        blank=True,
        null=True,
        help_text=_("Image size should be 1920 x 1080"),
    )

    class Meta:
        verbose_name = _("Sponsor Page")
        verbose_name_plural = _("Sponsor Page")

    def __str__(self) -> str:
        return self.title

file_cleanup.delete_file_on_model_delete(SponsorPage, "image")


class Sponsor(TimeStamp):
    name = models.CharField(max_length=255, verbose_name=_("Name"))
    level = models.CharField(
        max_length=255,
        verbose_name=_("Sponsorship Level"),
        choices=SponsorshipLevel.choices(),
    )
    logo = models.ImageField(
        upload_to="sponsors",
        verbose_name=_("Image"),
        blank=True,
        null=True,
    )
    url = models.URLField(verbose_name=_("URL"), blank=True)

    class Meta:
        verbose_name = _("Sponsor")
        verbose_name_plural = _("Sponsors")

    def __str__(self) -> str:
        return self.name

file_cleanup.delete_file_on_model_delete(Sponsor, "logo")


class SponsorshipPackage(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("Name"))
    level = models.CharField(
        max_length=255,
        verbose_name=_("Sponsorship Level"),
        choices=SponsorshipLevel.choices(),
    )
    description = models.TextField(verbose_name=_("Description"))
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name=_("Price"),
    )
    image = models.ImageField(
        upload_to="sponsors",
        verbose_name=_("Image"),
        blank=True,
        null=True,
    )
    order = models.PositiveIntegerField(verbose_name=_("Order"), default=0)
    featured = models.BooleanField(verbose_name=_("Featured"), default=False)

    class Meta:
        verbose_name = _("Sponsorship Package")
        verbose_name_plural = _("Sponsorship Packages")
        ordering = ["order"]

    def __str__(self) -> str:
        return self.name


file_cleanup.delete_file_on_model_delete(SponsorshipPackage, "image")


class SponsorshipApplication(TimeStamp):
    name = models.CharField(max_length=255, verbose_name=_("Name"))
    email = models.EmailField(verbose_name=_("Email"))
    phone = PhoneNumberField(verbose_name=_("Phone"))
    company = models.CharField(max_length=255, verbose_name=_("Company"))
    website = models.URLField(verbose_name=_("Website"), blank=True)
    level = models.CharField(
        max_length=255,
        verbose_name=_("Sponsorship Level"),
        choices=SponsorshipLevel.choices(),
    )
    message = models.TextField(verbose_name=_("Message"))
    package = models.ForeignKey(
        SponsorshipPackage,
        on_delete=models.CASCADE,
        verbose_name=_("Package"),
        related_name="package",
    )
    accepted = models.BooleanField(verbose_name=_("Accepted"), default=False)

    class Meta:
        verbose_name = _("Sponsorship Application")
        verbose_name_plural = _("Sponsorship Applications")

    def __str__(self) -> str:
        return self.name

class ResourceCategory(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("Name"))
    description = models.TextField(verbose_name=_("Description"), blank=True)
    created_date = models.DateTimeField(auto_now_add=True, verbose_name=_("Created Date"))
    updated_date = models.DateTimeField(auto_now=True, verbose_name=_("Updated"))

    class Meta:
        verbose_name = _("Resource Category")
        verbose_name_plural = _("Resource Categories")
        ordering = ["-created_date"]

    def __str__(self) -> str:
        return self.name

class Resource(models.Model):
    category = models.ForeignKey(
        ResourceCategory,
        on_delete=models.CASCADE,
        verbose_name=_("Category"),
        related_name="resources",
    )
    uuid = models.UUIDField(editable=False, unique=True, default=uuid.uuid4)
    title = models.CharField(max_length=255, verbose_name=_("Title"))
    difficulty = models.CharField(
        max_length=255,
        verbose_name=_("Difficulty"),
        choices=DificultyLevel.choices(),
        blank=True,
        default=DificultyLevel.EASY,
    )
    slug = models.SlugField(max_length=255, verbose_name=_("Slug"), unique=True, editable=False)
    description = HTMLField(verbose_name=_("Description"), blank=True)
    video = models.URLField(verbose_name=_("Video"), blank=True)
    created_date = models.DateTimeField(auto_now_add=True, verbose_name=_("Created Date"))
    updated_date = models.DateTimeField(auto_now=True, verbose_name=_("Updated"))

    class Meta:
        verbose_name = _("Resource")
        verbose_name_plural = _("Resources")
        ordering = ["-created_date"]

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
