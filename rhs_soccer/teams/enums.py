from enum import Enum

from django.utils.translation import gettext_lazy as _


class TeamLevel(Enum):
    VARSITY = "Varsity"
    JV = "JV"
    SOPHOMORE = "Sophmore"
    FRESHMAN = "Freshman"

    @classmethod
    def choices(cls):
        return [(key.value, key.value) for key in cls]

    @classmethod
    def choices_dict(cls):
        return {key.value: key.value for key in cls}


class Season(Enum):
    SEASON1 = "2024-2025"
    SEASON2 = "2025-2026"
    SEASON4 = "2026-2027"
    SEASON5 = "2027-2028"
    SEASON6 = "2028-2029"

    @classmethod
    def choices(cls):
        return [(key.value, key.value) for key in cls]

    @classmethod
    def choices_dict(cls):
        return {key.value: key.value for key in cls}


class TeamType(Enum):
    AWAY = _("Away")
    HOME = _("Home")

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]

    @classmethod
    def choices_dict(cls):
        return {key.value: key.name for key in cls}

    @classmethod
    def choices_dict_reverse(cls):
        return {key.name: key.value for key in cls}
