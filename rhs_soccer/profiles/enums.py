from enum import Enum

from django.utils.translation import gettext_lazy as _


class PlayerPosition(Enum):
    """
    Enum class for player positions.
    """

    GOALKEEPER = _("Goalkeeper")
    DEFENDER = _("Defender")
    MIDFIELDER = _("Midfielder")
    FORWARD = _("Forward")

    @classmethod
    def choices(cls):
        return tuple((i.value, i.value) for i in cls)

    @classmethod
    def choices_dict(cls):
        return {i.value: i.value for i in cls}

    @classmethod
    def choices_dict_reverse(cls):
        return {i.value: i for i in cls}


class PlayerStatus(Enum):
    """
    Enum class for player status.
    """

    ACTIVE = _("Active")
    INACTIVE = _("Inactive")
    RETIRED = _("Retired")
    TRANSFERRED = _("Transferred")
    RESIGNED = _("Resigned")
    SUSPENDED = _("Suspended")

    @classmethod
    def choices(cls):
        return tuple((i.value, i.value) for i in cls)

    @classmethod
    def choices_dict(cls):
        return {i.value: i.value for i in cls}

    @classmethod
    def choices_dict_reverse(cls):
        return {i.value: i for i in cls}


class PlayerGrade(Enum):
    """
    Enum class for player grades.
    """

    SIXTH = _("6th Grader")
    SEVENTH = _("7th Grader")
    EIGHTH = _("8th Grader")
    FRESHMAN = _("Freshman")
    SOPHOMORE = _("Sophomore")
    JUNIOR = _("Junior")
    SENIOR = _("Senior")

    @classmethod
    def choices(cls):
        return tuple((i.value, i.value) for i in cls)

    @classmethod
    def choices_dict(cls):
        return {i.value: i.value for i in cls}

    @classmethod
    def choices_dict_reverse(cls):
        return {i.value: i for i in cls}


class EmergencyContactRelationship(Enum):
    MOTHER = _("Mother")
    FATHER = _("Father")
    GRANDPARENT = _("Grandparent")
    SISTER = _("Sister")
    BROTHER = _("Brother")
    SON = _("Son")
    DAUGHTER = _("Daughter")
    FRIEND = _("Friend")
    SPOUSE = _("Spouse")
    NEIGHBOR = _("Neighbor")
    OTHER = _("Other")

    @classmethod
    def choices(cls):
        return [(key.value, key.value) for key in cls]

    @classmethod
    def choices_dict(cls):
        return {key.value: key.value for key in cls}

    @classmethod
    def choices_dict_reverse(cls):
        return {key.value: key for key in cls}
