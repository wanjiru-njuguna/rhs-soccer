from django.db.models.manager import Manager

from rhs_soccer.teams.enums import TeamLevel


class TeamManger(Manager):
    def varsity(self):
        return self.get_queryset().filter(level=TeamLevel.VARSITY).first()

    def jv(self):
        return self.get_queryset().filter(level=TeamLevel.JV).first()

    def freshman(self):
        return self.get_queryset().filter(level=TeamLevel.FRESHMAN).first()

    def sophomore(self):
        return self.get_queryset().filter(level=TeamLevel.SOPHOMORE).first()
