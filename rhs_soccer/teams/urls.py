from django.urls import path

from rhs_soccer.teams.views import freshman_team
from rhs_soccer.teams.views import jv_team
from rhs_soccer.teams.views import sophomore_team
from rhs_soccer.teams.views import team
from rhs_soccer.teams.views import team_page
from rhs_soccer.teams.views import varsity_team

app_name = "teams"

urlpatterns = [
    path("", team_page, name="team_page"),
    path("team/<uuid:team_id>", team, name="team"),
    path("varsity/", varsity_team, name="varsity"),
    path("jv/", jv_team, name="jv"),
    path("sophomore/", sophomore_team, name="sophomore"),
    path("freshman/", freshman_team, name="freshman"),
]
