from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

from rhs_soccer.events.models import Event

admin_group, created = Group.objects.get_or_create(name="Admin")
admin_group.save()

manager_group, created = Group.objects.get_or_create(name="Manager")
manager_group.save()

coach_group, created = Group.objects.get_or_create(name="Coach")
coach_group.save()

create_event = Permission.objects.get(
    codename="add_event",
    content_type=ContentType.objects.get_for_model(Event),
    )

admin_group.permissions.add(create_event)
admin_group.save()

manager_group.permissions.add(create_event)
manager_group.save()

coach_group.permissions.add(create_event)
coach_group.save()


edit_event = Permission.objects.get(
    codename="change_event",
    content_type=ContentType.objects.get_for_model(Event),
    )

manager_group.permissions.add(edit_event)
manager_group.save()

coach_group.permissions.add(edit_event)
coach_group.save()

delete_event = Permission.objects.get(
    codename="delete_event",
    content_type=ContentType.objects.get_for_model(Event),
    )

admin_group.permissions.add(delete_event)
admin_group.save()

coach_group.permissions.add(delete_event)
coach_group.save()

view_event = Permission.objects.get(
    codename="view_event",
    content_type=ContentType.objects.get_for_model(Event),
    )

admin_group.permissions.add(view_event)
admin_group.save()



