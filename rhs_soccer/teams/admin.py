from django.contrib import admin

from rhs_soccer.teams.models import Team
from rhs_soccer.teams.models import TeamPage

admin.site.register(TeamPage)
admin.site.register(Team)
