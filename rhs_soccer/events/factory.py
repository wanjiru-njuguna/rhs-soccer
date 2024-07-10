import factory
from django.utils.text import slugify
from factory import post_generation

from rhs_soccer.events.models import Attendee
from rhs_soccer.events.models import Event
from rhs_soccer.events.models import Location
from rhs_soccer.events.models import Volunteer
from rhs_soccer.users.enums import UserRoles
from rhs_soccer.users.models import User
from rhs_soccer.utils.common.enums import UsStates


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    email = factory.Faker("email")
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    role = factory.Faker("random_element", elements=[UserRoles.PLAYER.value, UserRoles.COACH.value, UserRoles.MANAGER.value])
    is_staff = False

    @post_generation
    def password(self, create, extracted, **kwargs):
        password = extracted or "defaultpassword"
        self.set_password(password)
        if create:
            self.save()



class LocationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Location

    name = factory.Faker("city")
    slug = factory.LazyAttribute(lambda o: slugify(o.name))
    address = factory.Faker("address")
    city = factory.Faker("city")
    state = factory.Faker("random_element", elements=[UsStates.MINNESOTA.value, UsStates.WISCONSIN.value])
    zip_code = factory.Faker("zipcode")
    email = factory.Faker("email")
    website = factory.Faker("url")
    description = factory.Faker("text")

class EventFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Event

    organizer = factory.SubFactory(UserFactory)
    title = factory.Faker("sentence")
    slug = factory.LazyAttribute(lambda o: slugify(o.title))
    event_type = factory.Faker("random_element", elements=["game", "practice", "meeting", "banquet"])
    location = factory.SubFactory(LocationFactory)
    start_date = factory.Faker("date_time_this_month", before_now=True, after_now=True)
    end_date = factory.Faker("date_time_this_month", before_now=True, after_now=True)
    description = factory.Faker("text")
    is_paid = factory.Faker("boolean", chance_of_getting_true=30)
    price = factory.Faker("random_int", min=10, max=50)
    need_volunteers = factory.Faker("boolean", chance_of_getting_true=30)
    volunteers_needed = factory.Faker("random_int", min=3, max=10)
    volunteer_credits = factory.Faker("random_int", min=1, max=5)
    is_published = factory.Faker("boolean", chance_of_getting_true=90)


class AttendeeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Attendee

    event = factory.SubFactory(EventFactory)
    user = factory.SubFactory(UserFactory)
    is_paid = factory.Faker("boolean", chance_of_getting_true=30)
    paid_date = factory.Faker("date_time_this_month", before_now=True, after_now=True)
    paid_amount = factory.Faker("random_int", min=10, max=50)


class VolunteerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Volunteer

    event = factory.SubFactory(EventFactory)
    user = factory.SubFactory(UserFactory)
    credits = factory.Faker("random_int", min=1, max=5)
