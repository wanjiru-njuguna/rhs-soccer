from django.urls import path

from rhs_soccer.events.views import event
from rhs_soccer.events.views import events
from rhs_soccer.events.views import login_modal
from rhs_soccer.events.views import volunteer_modal

app_name = "events"

urlpatterns = [
    path("", events, name="events"),
    path("<slug:event_slug>/", event, name="event"),
    path("login_modal/", login_modal, name="login_modal"),
    path("<slug:event_slug>/volunteer_modal/", volunteer_modal, name="volunteer_modal"),
]
