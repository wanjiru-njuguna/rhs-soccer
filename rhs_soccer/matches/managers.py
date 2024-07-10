from django.db import models
from django.db.models.functions import Now


class MatchManager(models.Manager):
    def finished(self):
        return self.get_queryset().filter(date__lt=Now())

    def upcoming(self):
        return self.get_queryset().filter(date__gte=Now())

    def today(self):
        return self.get_queryset().filter(date=Now())
