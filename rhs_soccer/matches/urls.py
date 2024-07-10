from django.urls import path

from rhs_soccer.matches.views import match
from rhs_soccer.matches.views import matches
from rhs_soccer.matches.views import past_matches
from rhs_soccer.matches.views import today_matches

app_name = "matches"

urlpatterns = [
    path("", matches, name="matches"),
    path("<uuid:match_id>/", match, name="match"),
    path("past/", past_matches, name="past_matches"),
    path("today/", today_matches, name="today_matches"),
]
