from typing import ClassVar
from django.utils import timezone

from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin, Group, Permission
from django.db import models
from django.db.models import BooleanField
from django.db.models import CharField
from django.db.models import EmailField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from rhs_soccer.users.enums import UserRoles

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    """
    Default custom user model for RHS Boys Soccer Club.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    # First and last name do not cover name patterns around the globe
    #id = models.UUIDField(default=uuid.uuid4, primary_key = True, editable=False, unique=True)    
    first_name = CharField(_("first name"), max_length=30, blank = True, null = True)
    last_name = CharField(_("last name"), max_length=30, blank = True,  null = True)
    email = EmailField(_("email address"), unique=True)
    role = CharField(
        _("Role"),
        max_length=50,
        choices=UserRoles.choices(),
        default=UserRoles.PLAYER.value,
    )
    username = None  # type: ignore[assignment]
    is_active = BooleanField(_("active"), default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    groups = models.ManyToManyField(
        Group,
        related_name="user_set",
        related_query_name="user",
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="user_set",
        related_query_name="user",
        blank=True,
    )
    date_joined = models.DateTimeField(default=timezone.now)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects: ClassVar[UserManager] = UserManager()

    def get_absolute_url(self) -> str:
        """Get URL for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"pk": self.id})

    def __str__(self) -> str:
        return self.email

    def get_full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"
