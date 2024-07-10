from django.contrib import admin

from rhs_soccer.profiles.models import Address
from rhs_soccer.profiles.models import Coach
from rhs_soccer.profiles.models import Manager
from rhs_soccer.profiles.models import Parent
from rhs_soccer.profiles.models import Player
from rhs_soccer.profiles.models import Profile


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ["profile", "position", "jeresy_number", "team", "is_published"]
    list_editable = ["position", "jeresy_number", "team", "is_published"]
    list_filter = ["position", "status"]
    ordering = ["id"]
    fields = ["profile", "position", "jeresy_number", "grade",  "status", "bio"]



admin.site.register(Address)
admin.site.register(Parent)
admin.site.register(Coach)
admin.site.register(Manager)
admin.site.register(Profile)
