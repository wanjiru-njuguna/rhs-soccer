from enum import Enum

from django.utils.translation import gettext_lazy as _


class UserRoles(Enum):
    """
    Enum class for user roles.
    """

    ADMIN = _("Admin")
    PLAYER = _("Player")
    COACH = _("Coach")
    MANAGER = _("Manager")
    REFEREE = _("Referee")
    PARENT = _("Parent")
    VOLUNTEER = _("Volunteer")

    @classmethod
    def choices(cls):
        return tuple((i.value, i.value) for i in cls)

    @classmethod
    def choices_dict(cls):
        return {i.value: i.value for i in cls}
