from django.db import models
from django.utils.translation import gettext_lazy as _


class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created At"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Updated At"))

    class Meta:
        abstract = True


class AuditTracking(TimeStamp):
    created_by = models.ForeignKey(
        "users.User",
        on_delete=models.SET_NULL,
        related_name="%(app_label)s_%(class)s_created_by",
        blank=True,
        null=True,
        verbose_name=_("Created By"),
    )
    updated_by = models.ForeignKey(
        "users.User",
        on_delete=models.SET_NULL,
        related_name="%(app_label)s_%(class)s_updated_by",
        blank=True,
        null=True,
        verbose_name=_("Updated By"),
    )

    class Meta:
        abstract = True
