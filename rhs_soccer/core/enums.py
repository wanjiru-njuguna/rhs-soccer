from enum import Enum

from django.utils.translation import gettext_lazy as _


class SocialMediaPlatform(Enum):
    FACEBOOK = _("Facebook")
    TWITTER = _("Twitter")
    INSTAGRAM = _("Instagram")
    YOUTUBE = _("Youtube")
    LINKEDIN = _("LinkedIn")
    TIKTOK = _("TikTok")

    @classmethod
    def choices(cls):
        return tuple((i.value, i.value) for i in cls)

    @classmethod
    def choices_dict(cls):
        return {i.value: i.name for i in cls}

    @classmethod
    def choices_dict_reverse(cls):
        return {i.name: i.value for i in cls}

class SponsorshipLevel(Enum):
    PLATINUM = _("Platinum")
    GOLD = _("Gold")
    SILVER = _("Silver")
    BRONZE = _("Bronze")

    @classmethod
    def choices(cls):
        return tuple((i.value, i.value) for i in cls)

    @classmethod
    def choices_dict(cls):
        return {i.value: i.value for i in cls}

    @classmethod
    def choices_dict_reverse(cls):
        return {i.name: i.value for i in cls}

class OfficerPosition(Enum):
    PRESIDENT = _("President")
    VICE_PRESIDENT = _("Vice President")
    SECRETARY = _("Secretary")
    TREASURER = _("Treasurer")
    MEMBER_AT_LARGE = _("Member at Large")
    PLAYER_OF_THE_MONTH = _("Player of the Month")
    COACH_OF_THE_MONTH = _("Coach of the Month")
    REFEREE_OF_THE_MONTH = _("Referee of the Month")

    @classmethod
    def choices(cls):
        return tuple((i.value, i.value) for i in cls)

    @classmethod
    def choices_dict(cls):
        return {i.value: i.value for i in cls}

    @classmethod
    def choices_dict_reverse(cls):
        return {i.name: i.value for i in cls}

class DificultyLevel(Enum):
    EASY = _("Easy")
    MEDIUM = _("Medium")
    HARD = _("Hard")

    @classmethod
    def choices(cls):
        return tuple((i.value, i.value) for i in cls)

    @classmethod
    def choices_dict(cls):
        return {i.value: i.value for i in cls}

    @classmethod
    def choices_dict_reverse(cls):
        return {i.name: i.value for i in cls}
