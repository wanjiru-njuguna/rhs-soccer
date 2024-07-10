from django import forms

from rhs_soccer.events.models import Volunteer


class VolunteerForm(forms.ModelForm):
    class Meta:
        model = Volunteer
        fields = ["event", "user"]
        widgets = {
            "event": forms.HiddenInput(),
            "user": forms.HiddenInput(),
        }
        labels = {
            "event": "Event",
            "user": "User",
        }
