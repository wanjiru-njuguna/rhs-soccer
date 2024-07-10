from django.contrib import admin

from rhs_soccer.events.models import Attendee
from rhs_soccer.events.models import Event
from rhs_soccer.events.models import EventPage
from rhs_soccer.events.models import Location
from rhs_soccer.events.models import Volunteer

admin.site.register(Event)
admin.site.register(Location)
admin.site.register(Attendee)
admin.site.register(EventPage)
admin.site.register(Volunteer)
