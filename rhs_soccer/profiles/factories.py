import factory

from rhs_soccer.profiles.models import Address
from rhs_soccer.utils.common.enums import UsStates


class AddressFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Address

    address = factory.Faker("address")
    address2 = factory.Faker("address")
    city = factory.Faker("city")
    state = factory.Faker("random_element", elements=[UsStates.MINNESOTA.value, UsStates.WISCONSIN.value])
    zip_code = factory.Faker("zipcode")
