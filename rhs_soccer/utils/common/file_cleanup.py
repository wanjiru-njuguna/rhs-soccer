from django.db.models.signals import post_delete
from django.dispatch import receiver


def delete_file_on_model_delete(model, file_field):
    @receiver(post_delete, sender=model)
    def delete_file(sender, instance, **kwargs):
        file = getattr(instance, file_field)
        if file:
            file.delete(False)
