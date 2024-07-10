from enum import Enum

from django.utils.translation import gettext_lazy as _


class RecurringType(Enum):
    DAILY = "daily"
    WEEKLY = "weekly"
    MONTHLY = "monthly"
    YEARLY = "yearly"

    @classmethod
    def choices(cls):
        return [(key.value, _(key.name.capitalize())) for key in cls]

    @classmethod
    def choices_dict(cls):
        return {key.value: _(key.name.capitalize()) for key in cls}


class EvenType(Enum):
    GAME = "game"
    PRACTICE = "practice"
    TOURNAMENT = "tournament"
    MEETING = "meeting"
    BANQUET = "banquet"
    AWARD = "award"
    OTHER = "other"

    @classmethod
    def choices(cls):
        return [(key.value, _(key.name.capitalize())) for key in cls]

    @classmethod
    def choices_dict(cls):
        return {key.value: _(key.name.capitalize()) for key in cls}
