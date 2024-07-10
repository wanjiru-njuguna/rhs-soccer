from django.contrib import admin

from rhs_soccer.matches.models import Highlight
from rhs_soccer.matches.models import Match
from rhs_soccer.matches.models import Venue

admin.site.register(Venue)
admin.site.register(Match)
admin.site.register(Highlight)
