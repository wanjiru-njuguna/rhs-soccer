import uuid
from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from solo.models import SingletonModel

from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField
from wagtail.snippets.models import register_snippet
from modelcluster.models import ClusterableModel

from rhs_soccer.core.enums import DificultyLevel
from rhs_soccer.core.enums import OfficerPosition
from rhs_soccer.core.enums import SponsorshipLevel
from rhs_soccer.utils.common import file_cleanup
from rhs_soccer.utils.common.singelton_page import SingletonPage

from rhs_soccer.utils.common.enums import UsStates
from rhs_soccer.utils.helpers.models import TimeStamp


@register_snippet
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
class SiteSettings(SingletonModel):
    name = models.CharField(max_length=255, verbose_name=_("Name"), blank=True)
    short_name = models.CharField(max_length=50, verbose_name=_("Short Name"), blank=True)
    tagline = models.CharField(max_length=255, verbose_name=_("Tagline"), blank=True)
    logo = models.ForeignKey(
        'wagtailimages.Image',
        verbose_name=_("Logo"),
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name = "+"
    )
    dark_logo = models.ForeignKey(
        'wagtailimages.Image',
        verbose_name=_("Dark Logo"),
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name = "+"
    )
    favicon = models.ForeignKey(
        'wagtailimages.Image',
        verbose_name=_("Favicon"),
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )
    phone = PhoneNumberField(max_length=255, verbose_name=_("Phone"))
    email = models.CharField(max_length=255, verbose_name=_("Email"))
    address = models.ForeignKey(
        'Address',
        on_delete=models.SET_NULL,
        related_name="site_address",
        blank=True,
        null=True,
    )
    social_media = models.OneToOneField(
        'SocialMedia',
        blank=True,
        null=True,
        verbose_name=_("Social Media"),
        on_delete=models.SET_NULL,
        related_name="social_media",
    )
    description = models.TextField(verbose_name=_("Description"), blank=True)
    keywords = models.TextField(verbose_name=_("Keywords"), blank=True)
    fund_raising_mode = models.BooleanField(_("Fund Raising Mode"), default=False)

    panels = [
        FieldPanel('name'),
        FieldPanel('short_name'),
        FieldPanel('tagline'),
        FieldPanel('logo'),
        FieldPanel('dark_logo'),
        FieldPanel('favicon'),
        FieldPanel('phone'),
        FieldPanel('email'),
        FieldPanel('address'),
        FieldPanel('social_media'),
        FieldPanel('description'),
        FieldPanel('keywords'),
        FieldPanel('fund_raising_mode'),
    ]

    class Meta:
        verbose_name = _("Site Settings")
        verbose_name_plural = _("Site Settings")

    def __str__(self) -> str:
        return self.name

@register_snippet
class SocialMedia(SingletonModel):
    site = models.ForeignKey(
        'SiteSettings',
        on_delete=models.CASCADE,
        verbose_name=_("Site"),
        related_name="social_media_site",
    )
    facebook = models.URLField(verbose_name=_("Facebook URL"), blank=True)
    twitter = models.URLField(verbose_name=_("Twitter URL"), blank=True)
    instagram = models.URLField(verbose_name=_("Instagram URL"), blank=True)
    linkedin = models.URLField(verbose_name=_("LinkedIn URL"), blank=True)
    youtube = models.URLField(verbose_name=_("YouTube URL"), blank=True)

    panels = [
        FieldPanel('site'),
        FieldPanel('facebook'),
        FieldPanel('twitter'),
        FieldPanel('instagram'),
        FieldPanel('linkedin'),
        FieldPanel('youtube'),
    ]

    class Meta:
        verbose_name = _("Social Media")
        verbose_name_plural = _("Social Media")

    def __str__(self):
        return f"{self.site.name} Social Media"

class AboutPage(Page):
    subtitle = models.CharField(max_length=255, verbose_name=_("Subtitle"), blank=True)
    content = RichTextField(verbose_name=_("Content"), blank=True)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text=_("Image size should be 1920 x 1080"),
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created at"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Updated at"))

    content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
        FieldPanel('content'),
        FieldPanel('image'),
    ]

    class Meta:
        verbose_name = _("About Page")
        verbose_name_plural = _("About Page")

    def __str__(self) -> str:
        return self.title

class ContactPage(Page):
   # title = models.CharField(max_length=255, verbose_name=_("Title"))
    subtitle = models.CharField(max_length=255, verbose_name=_("Subtitle"))
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name=_("Image")
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created at"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Updated at"))

    content_panels = Page.content_panels + [
        FieldPanel('title'),
        FieldPanel('subtitle'),
        FieldPanel('image'),
       

    ]

    class Meta:
        verbose_name = _("Contact Page")
        verbose_name_plural = _("Contact Page")

    def __str__(self) -> str:
        return self.title

@register_snippet
class Contact(ClusterableModel):
    first_name = models.CharField(max_length=255, verbose_name=_("First Name"))
    last_name = models.CharField(max_length=255, verbose_name=_("Last Name"))
    email = models.EmailField(verbose_name=_("Email"))
    phone = PhoneNumberField(verbose_name=_("Phone"), blank=True)
    message = models.TextField(verbose_name=_("Message"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created at"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Updated at"))

    panels = [
        FieldPanel('first_name'),
        FieldPanel('last_name'),
        FieldPanel('email'),
        FieldPanel('phone'),
        FieldPanel('message'),
        
    ]

    class Meta:
        verbose_name = _("Contact")
        verbose_name_plural = _("Contacts")

    def __str__(self) -> str:
        return self.email


class PrivacyPolicyPage(SingletonPage):
    subtitle = models.CharField(max_length=255, verbose_name=_("Subtitle"), blank=True)
    content = RichTextField(verbose_name=_("Content"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created At"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Updated At"))

    content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
        FieldPanel('content'),
    ]

    class Meta:
        verbose_name = _("Privacy Policy Page")
        verbose_name_plural = _("Privacy Policy Page")

    def __str__(self) -> str:
        return self.title


class TermsOfServicePage(SingletonPage):
    #title = models.CharField(max_length=255, verbose_name=_("Title"))
    subtitle = models.CharField(max_length=255, verbose_name=_("Subtitle"), blank=True)
    content = RichTextField(verbose_name=_("Content"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created At"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Updated At"))

    content_panels = Page.content_panels + [
        FieldPanel('title'),
        FieldPanel('subtitle'),
        FieldPanel('content'),
    ]


    class Meta:
        verbose_name = _("Terms of Service Page")
        verbose_name_plural = _("Terms of Service Page")

    def __str__(self) -> str:
        return self.title

class BoosterPage(SingletonPage):
    #title = models.CharField(max_length=255, verbose_name=_("Title"))
    subtitle = models.CharField(max_length=255, verbose_name=_("Subtitle"), blank=True)
    heading = models.CharField(max_length=255, verbose_name=_("Heading"))
    content = RichTextField(verbose_name=_("Content"))
    image = models.ForeignKey(
       'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name=_("Image")
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created At"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Updated At"))
    content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
        FieldPanel('heading'),
        FieldPanel('content'),
        FieldPanel('image'),
    ]

    class Meta:
        verbose_name = _("Booster Page")
        verbose_name_plural = _("Booster Page")

    def __str__(self) -> str:
        return self.title

file_cleanup.delete_file_on_model_delete(BoosterPage, "image")

@register_snippet
class BoosterOfficer(ClusterableModel):
    first_name = models.CharField(max_length=255, verbose_name=_("First Name"))
    last_name = models.CharField(max_length=255, verbose_name=_("Last Name"))
    title = models.CharField(
        max_length=255,
        verbose_name=_("Title"),
        choices=OfficerPosition.choices(),
        blank=True)
    email = models.EmailField(verbose_name=_("Email"))
    phone = PhoneNumberField(max_length=255, verbose_name=_("Phone"))
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name=_("Image")
    )
    bio = RichTextField(verbose_name=_("Bio"), blank=True)

    panels = [
        FieldPanel('first_name'),
        FieldPanel('last_name'),
        FieldPanel('title'),
        FieldPanel('email'),
        FieldPanel('phone'),
        FieldPanel('image'),
        FieldPanel('bio'),
    ]
    class Meta:
        verbose_name = _("Booster Officer")
        verbose_name_plural = _("Booster Officers")

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

file_cleanup.delete_file_on_model_delete(BoosterOfficer, "image")


class SponsorPage(SingletonPage):
    #title = models.CharField(max_length=255, verbose_name=_("Title"))
    subtitle = models.CharField(max_length=255, verbose_name=_("Subtitle"), blank=True)
    heading = models.CharField(max_length=255, verbose_name=_("Heading"), blank=True)
    content = RichTextField(verbose_name=_("Content"), blank=True)
    cta = models.CharField(max_length=255, verbose_name=_("Call to Action"), blank=True)
    image = models.ForeignKey(
       'wagtailimages.Image',
        verbose_name=_("Image"),
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        help_text=_("Image size should be 1920 x 1080"),
    )
    content_panels = Page.content_panels + [
        FieldPanel('title'),
        FieldPanel('subtitle'),
        FieldPanel('heading'),
        FieldPanel('content'),
        FieldPanel('cta'),
        FieldPanel('image'),
    ]
    class Meta:
        verbose_name = _("Sponsor Page")
        verbose_name_plural = _("Sponsor Page")

    def __str__(self) -> str:
        return self.title

file_cleanup.delete_file_on_model_delete(SponsorPage, "image")

@register_snippet
class Sponsor(TimeStamp, ClusterableModel):
    name = models.CharField(max_length=255, verbose_name=_("Name"))
    level = models.CharField(
        max_length=255,
        verbose_name=_("Sponsorship Level"),
        choices=SponsorshipLevel.choices(),
    )
    logo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name=_("Image")
    )
    url = models.URLField(verbose_name=_("URL"), blank=True)
    panels = [
        FieldPanel('name'),
        FieldPanel('level'),
        FieldPanel('logo'),
        FieldPanel('url'),
    ]

    class Meta:
        verbose_name = _("Sponsor")
        verbose_name_plural = _("Sponsors")

    def __str__(self) -> str:
        return self.name

file_cleanup.delete_file_on_model_delete(Sponsor, "logo")

@register_snippet
class SponsorshipPackage(ClusterableModel):
    name = models.CharField(max_length=255, verbose_name=_("Name"))
    level = models.CharField(
        max_length=255,
        verbose_name=_("Sponsorship Level"),
        choices=SponsorshipLevel.choices(),
    )
    description = RichTextField(verbose_name=_("Description"))
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name=_("Price"),
    )
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name=_("Image")
    )
    order = models.PositiveIntegerField(verbose_name=_("Order"), default=0)
    featured = models.BooleanField(verbose_name=_("Featured"), default=False)
    panels = [
        FieldPanel('name'),
        FieldPanel('level'),
        FieldPanel('description'),
        FieldPanel('price'),
        FieldPanel('image'),
        FieldPanel('order'),
        FieldPanel('featured'),
    ]

    class Meta:
        verbose_name = _("Sponsorship Package")
        verbose_name_plural = _("Sponsorship Packages")
        ordering = ["order"]

    def __str__(self) -> str:
        return self.name


file_cleanup.delete_file_on_model_delete(SponsorshipPackage, "image")

@register_snippet
class SponsorshipApplication(TimeStamp, ClusterableModel):
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
    panels = [
        FieldPanel('name'),
        FieldPanel('email'),
        FieldPanel('phone'),
        FieldPanel('company'),
        FieldPanel('website'),
        FieldPanel('level'),
        FieldPanel('message'),
        FieldPanel('package'),
        FieldPanel('accepted'),
    ]
    class Meta:
        verbose_name = _("Sponsorship Application")
        verbose_name_plural = _("Sponsorship Applications")

    def __str__(self) -> str:
        return self.name
@register_snippet
class ResourceCategory(ClusterableModel):
    name = models.CharField(max_length=255, verbose_name=_("Name"))
    description = models.TextField(verbose_name=_("Description"), blank=True)
    created_date = models.DateTimeField(auto_now_add=True, verbose_name=_("Created Date"))
    updated_date = models.DateTimeField(auto_now=True, verbose_name=_("Updated"))
    panels = [
        FieldPanel('name'),
        FieldPanel('description'),
    ]
    class Meta:
        verbose_name = _("Resource Category")
        verbose_name_plural = _("Resource Categories")
        ordering = ["-created_date"]

    def __str__(self) -> str:
        return self.name
@register_snippet
class Resource(ClusterableModel):
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
    description = RichTextField(verbose_name=_("Description"), blank=True)
    video = models.URLField(verbose_name=_("Video"), blank=True)
    created_date = models.DateTimeField(auto_now_add=True, verbose_name=_("Created Date"))
    updated_date = models.DateTimeField(auto_now=True, verbose_name=_("Updated"))
    panels = [
        FieldPanel('category'),
        FieldPanel('uuid'),
        FieldPanel('title'),
        FieldPanel('difficulty'),
        FieldPanel('slug'),
        FieldPanel('description'),
        FieldPanel('video'),
    ]

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
