from enum import Enum

from django.utils.translation import gettext_lazy as _


class DonationType(Enum):
    ONE_TIME = _("One Time")
    RECURRING = _("Recurring")

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)
