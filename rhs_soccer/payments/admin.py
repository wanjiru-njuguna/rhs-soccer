from django.contrib import admin

from rhs_soccer.payments.models import Donation
from rhs_soccer.payments.models import PlayerFee
from rhs_soccer.payments.models import DonationPage
from rhs_soccer.payments.models import Campaign

admin.site.register(DonationPage)
admin.site.register(Campaign)
admin.site.register(Donation)
admin.site.register(PlayerFee)