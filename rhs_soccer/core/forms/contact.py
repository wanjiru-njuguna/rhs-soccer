from django import forms
from django.utils.translation import gettext_lazy as _
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV3
from phonenumber_field.formfields import PhoneNumberField


class ContactForm(forms.Form):
    name = forms.CharField(label=_("Name"), max_length=100)
    email = forms.EmailField(label=_("Email"))
    phone = PhoneNumberField(label=_("Phone"), required=False)
    subject = forms.CharField(label=_("Subject"), max_length=100)
    message = forms.CharField(label=_("Message"), widget=forms.Textarea)
    captcha = ReCaptchaField(
        label="",
        widget=ReCaptchaV3(
            attrs={
                "required": True,
            },
        ),
    )

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
        self.fields["subject"].widget.attrs.update(
            {
                "placeholder": _("Subject"),
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
                "class": "form-control",
            },
        )

    def clean(self):
        cleaned_data = super().clean()
        if not cleaned_data.get("phone") and not cleaned_data.get("email"):
            raise forms.ValidationError(
                _("You must provide either an email or phone number."),
            )
        return cleaned_data
