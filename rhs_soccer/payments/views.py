from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
from django.utils.translation import gettext_lazy as _

from rhs_soccer.payments.filters import DonationFilter
from rhs_soccer.payments.models import Donation
from rhs_soccer.payments.models import PlayerFee


@user_passes_test(lambda u: u.is_staff)
def donations(request):
    donations_filter = DonationFilter(
        request.GET,
        queryset=Donation.objects.all(),
        )
    title = _("Donations")
    context = {"filter": donations_filter, "title": title}
    return render(request, "donations/donations.html", context)


@login_required
def my_donations(request):
    donations = Donation.objects.filter(user=request.user)
    title = _("My Donations")
    context = {"donations": donations, "title": title}
    return render(request, "donations/donations.html", context)


@login_required
def player_fees(request):
    player_fees = PlayerFee.objects.all()
    title = _("Player Fees")
    context = {"player_fees": player_fees, "title": title}
    return render(request, "donations/fees.html", context)

@login_required
def my_player_fees(request):
    player_fees = PlayerFee.objects.filter(user=request.user)
    title = _("My Player Fees")
    context = {"player_fees": player_fees, "title": title}
    return render(request, "donations/fees.html", context)
