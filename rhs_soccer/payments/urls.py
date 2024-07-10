from django.urls import path

from rhs_soccer.payments.views import donations
from rhs_soccer.payments.views import my_donations
from rhs_soccer.payments.views import player_fees
from rhs_soccer.payments.views import my_player_fees

app_name = "payments"

urlpatterns = [
    path("", donations, name="donations"),
    path("my-donations/", my_donations, name="my_donations"),
    path("fees/", player_fees, name="player_fees"),
    path("my-fees/", my_player_fees, name="my_player_fees"),
]
