import django_filters
from django.utils.translation import gettext_lazy as _

from rhs_soccer.payments.enums import DonationType
from rhs_soccer.payments.models import Donation


class DonationFilter(django_filters.FilterSet):
    class Meta:
        donation_type = django_filters.ChoiceFilter(
            field_name="donation_type",
            choices=DonationType.choices(),
            label=_("Donation Type"),
            lookup_expr="exact",
            empty_label=_("Any"),
        )
        model = Donation
        fields = {
            "user": ["exact"],
            "date": ["exact", "gt", "lt"],
        }
