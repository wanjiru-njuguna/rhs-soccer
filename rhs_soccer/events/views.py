from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render

from rhs_soccer.events.forms.volunteer import VolunteerForm
from rhs_soccer.events.models import Attendee
from rhs_soccer.events.models import Event
from rhs_soccer.events.models import EventPage
from rhs_soccer.events.models import Volunteer


def events(request):
    events = Event.objects.filter(is_published=True)
    # upcoming = bool(events.exists())
    event_page = EventPage.objects.first()
    context = {
        "events": events,
        "title": "Events",
        # "upcoming": upcoming,
        "event_page": event_page,
    }
    return render(request, "events/events.html", context)


def event(request, event_slug):
    event = get_object_or_404(Event, slug=event_slug)
    volunteer_count = Volunteer.objects.per_event(event_slug)
    attendee_count = Attendee.objects.per_event(event_slug)
    volunteers_still_needed = event.volunteers_needed - volunteer_count

    context = {
        "event": event,
        "title": event.title,
        "page_title": event.title,
        "event_page": EventPage.objects.first(),
        "volunteer_count": volunteer_count,
        "attendee_count": attendee_count,
        "volunteers_still_needed": volunteers_still_needed,
        "is_organizer": request.user == event.organizer,
        "is_attendee": event.attendees.filter(user=request.user).exists(),
        "is_paid": event.attendees.filter(user=request.user, is_paid=True).exists(),
    }

    return render(request, "events/event.html", context)


def login_modal(request):
    if not request.user.is_authenticated:
        return JsonResponse({"authenticated": False, "redirect_to": "/accounts/login/"})

    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({"success": True})
        return JsonResponse({"success": False, "message": "Invalid email or password"})

    # Render modal content template
    return render(request, "account/login_modal.html")


def volunteer_modal(request, event_id):
    event = get_object_or_404(Event, slug=event_id)
    user = request.user
    if request.method == "POST":
        volunteer_form = VolunteerForm(request.POST)
        if volunteer_form.is_valid():
            volunteer = volunteer_form.save(commit=False)
            volunteer.event = event
            volunteer.user = user
            volunteer.save()
        return redirect(event)
    context = {
        "form": VolunteerForm(),
        "event": event,
        "user": user,
    }
    return render(request, "events/event.html", context)
