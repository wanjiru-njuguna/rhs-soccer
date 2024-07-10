from enum import Enum
from django.utils.translation import gettext_lazy as _

class MatchHighlight(Enum):
    GOAL = _("Goal")
    ASSIST = _("Assist")
    SAVE = _("Save")
    YELLOW_CARD = _("Yellow Card")
    RED_CARD = _("Red Card")
    PENALTY = _("Penalty")
    FREE_KICK = _("Free Kick")
    CORNER_KICK = _("Corner Kick")
    THROW_IN = _("Throw In")
    GOAL_KICK = _("Goal Kick")
    PENALTY_KICK = _("Penalty Kick")
    OWN_GOAL = _("Own Goal")
    HAT_TRICK = _("Hat Trick")
    CLEAN_SHEET = _("Clean Sheet")

    @classmethod
    def choices(cls):
        return tuple((i.value, i.value) for i in cls)

    @classmethod
    def choices_dict(cls):
        return {i.value: i.name for i in cls}

    @classmethod
    def choices_dict_reverse(cls):
        return {i.name: i.value for i in cls}