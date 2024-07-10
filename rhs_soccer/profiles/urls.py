from django.urls import path

from rhs_soccer.profiles.views import coach
from rhs_soccer.profiles.views import coaches
from rhs_soccer.profiles.views import player
from rhs_soccer.profiles.views import players

app_name = "profiles"

urlpatterns = [
    path("coaches/", coaches, name="coaches"),
    path("coaches/<int:coach_id>/", coach, name="coach"),
    path("players/", players, name="players"),
    path("players/<int:id>/", player, name="player"),
]
