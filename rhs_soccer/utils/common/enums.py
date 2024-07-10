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
        return tuple((i.value, i.name) for i in cls)

    @classmethod
    def choices_dict(cls):
        return {i.value: i.name for i in cls}

    @classmethod
    def choices_dict_reverse(cls):
        return {i.name: i.value for i in cls}


class UserType(Enum):
    ADMIN = _("Admin")
    COACH = _("Coach")
    PLAYER = _("Player")
    PARENT = _("Parent")
    FAN = _("Fan")

    @classmethod
    def choices(cls):
        return tuple((i.value, i.name) for i in cls)

    @classmethod
    def choices_dict(cls):
        return {i.value: i.name for i in cls}

    @classmethod
    def choices_dict_reverse(cls):
        return {i.name: i.value for i in cls}


class UsStates(Enum):
    ALABAMA = _("Alabama")
    ALASKA = _("Alaska")
    ARIZONA = _("Arizona")
    ARKANSAS = _("Arkansas")
    CALIFORNIA = _("California")
    COLORADO = _("Colorado")
    CONNECTICUT = _("Connecticut")
    DELAWARE = _("Delaware")
    FLORIDA = _("Florida")
    GEORGIA = _("Georgia")
    HAWAII = _("Hawaii")
    IDAHO = _("Idaho")
    ILLINOIS = _("Illinois")
    INDIANA = _("Indiana")
    IOWA = _("Iowa")
    KANSAS = _("Kansas")
    KENTUCKY = _("Kentucky")
    LOUISIANA = _("Louisiana")
    MAINE = _("Maine")
    MARYLAND = _("Maryland")
    MASSACHUSETTS = _("Massachusetts")
    MICHIGAN = _("Michigan")
    MINNESOTA = _("Minnesota")
    MISSISSIPPI = _("Mississippi")
    MISSOURI = _("Missouri")
    MONTANA = _("Montana")
    NEBRASKA = _("Nebraska")
    NEVADA = _("Nevada")
    NEW_HAMPSHIRE = _("New Hampshire")
    NEW_JERSEY = _("New Jersey")
    NEW_MEXICO = _("New Mexico")
    NEW_YORK = _("New York")
    NORTH_CAROLINA = _("North Carolina")
    NORTH_DAKOTA = _("North Dakota")
    OHIO = _("Ohio")
    OKLAHOMA = _("Oklahoma")
    OREGON = _("Oregon")
    PENNSYLVANIA = _("Pennsylvania")
    RHODE_ISLAND = _("Rhode Island")
    SOUTH_CAROLINA = _("South Carolina")
    SOUTH_DAKOTA = _("South Dakota")
    TENNESSEE = _("Tennessee")
    TEXAS = _("Texas")
    UTAH = _("Utah")
    VERMONT = _("Vermont")
    VIRGINIA = _("Virginia")
    WASHINGTON = _("Washington")
    WEST_VIRGINIA = _("West Virginia")
    WISCONSIN = _("Wisconsin")
    WYOMING = _("Wyoming")

    @classmethod
    def choices(cls):
        return tuple((i.value, i.value) for i in cls)

    @classmethod
    def choices_dict(cls):
        return {i.value: i.name for i in cls}

    @classmethod
    def choices_dict_reverse(cls):
        return {i.name: i.value for i in cls}


class UsRegions(Enum):
    NORTHEAST = _("Northeast")
    MIDWEST = _("Midwest")
    SOUTH = _("South")
    WEST = _("West")

    @classmethod
    def choices(cls):
        return tuple((i.value, i.name) for i in cls)

    @classmethod
    def choices_dict(cls):
        return {i.value: i.name for i in cls}

    @classmethod
    def choices_dict_reverse(cls):
        return {i.name: i.value for i in cls}
