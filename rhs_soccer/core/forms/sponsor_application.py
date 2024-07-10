from django import forms
from django.utils.translation import gettext_lazy as _
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV3
from phonenumber_field.formfields import PhoneNumberField

from rhs_soccer.core.enums import SponsorshipLevel
from rhs_soccer.core.models import SponsorshipApplication


class SponsorshipApplicationForm(forms.ModelForm):
    name = forms.CharField(label=_("Name"), max_length=100)
    email = forms.EmailField(label=_("Email"))
    phone = PhoneNumberField(label=_("Phone"), required=False)
    company = forms.CharField(label=_("Company"), max_length=100)
    website = forms.URLField(label=_("Website"), required=False)
    level = forms.ChoiceField(
        label=_("Sponsorship Level"),
        choices=SponsorshipLevel.choices(),
        initial=SponsorshipLevel.PLATINUM.value,
    )
    message = forms.CharField(label=_("Message"), widget=forms.Textarea)
    captcha = ReCaptchaField(
        label="",
        widget=ReCaptchaV3(
            attrs={
                "required": True,
            },
        ),
    )

    class Meta:
        model = SponsorshipApplication
        fields = [
            "name",
            "email",
            "phone",
            "company",
            "level",
            "website",
            "message",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["name"].widget.attrs.update(
            {
                "placeholder": _("Your name"),
                "error_messages": {
                    "required": _("Please enter your name."),
                    "max_length": _("Your name is too long."),
                },
            },
        )
        self.fields["email"].widget.attrs.update(
            {
                "placeholder": _("Your email"),
                "error_messages": {
                    "required": _("Please enter your email."),
                    "invalid": _("Please enter a valid email."),
                },
            },
        )
        self.fields["phone"].widget.attrs.update(
            {
                "placeholder": _("Your phone number"),
            },
        )
        self.fields["company"].widget.attrs.update(
            {
                "placeholder": _("Your company"),
                "error_messages": {
                    "required": _("Please enter your company."),
                    "max_length": _("Your company name is too long."),
                },
            },
        )
        self.fields["website"].widget.attrs.update(
            {
                "placeholder": _("Your website"),
            },
        )
        self.fields["level"].widget.attrs.update(
            {
                "placeholder": _("Sponsorship Level"),
            },
        )
        self.fields["message"].widget.attrs.update(
            {
                "placeholder": _("Your message"),
                "required": True,
            },
        )
        self.fields["captcha"].widget.attrs.update(
            {
                "required": True,
            },
        )
