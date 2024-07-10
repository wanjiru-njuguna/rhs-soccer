from django.db.models.signals import post_save
from django.dispatch import receiver

from rhs_soccer.profiles.models import Coach
from rhs_soccer.profiles.models import Manager
from rhs_soccer.profiles.models import Parent
from rhs_soccer.profiles.models import Player
from rhs_soccer.profiles.models import Profile
from rhs_soccer.users.enums import UserRoles
from rhs_soccer.users.models import User


@receiver(post_save, sender=User)
def create_profile_and_role(sender, instance, created, **kwargs):
    if created:
        profile = Profile.objects.create(user=instance)
        if instance.role == UserRoles.PLAYER.value:
            Player.objects.create(profile=profile)
        elif instance.role == UserRoles.COACH.value:
            Coach.objects.create(profile=profile)
        elif instance.role == UserRoles.MANAGER.value:
            Manager.objects.create(profile=profile)
        elif instance.role == UserRoles.PARENT.value:
            Parent.objects.create(profile=profile)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
