from django.db.models import Count
from django.db.models import Manager


class EventManager(Manager):
    def with_attendee_count(self):
        return self.annotate(attendees_count=Count("attendees"))

    def with_volunteer_count(self):
        return self.annotate(volunteers_count=Count("volunteers"))

class AttendeeManager(Manager):
    def per_event(self, event_id):
        return self.filter(event__slug=event_id).count()

class VolunteerManager(Manager):
    def per_event(self, event_id):
        return self.filter(event__slug=event_id).count()
