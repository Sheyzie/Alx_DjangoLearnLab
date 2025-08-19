from django.contrib.contenttypes.models import ContentType

from .models import Notification


def create_notification(recipient, actor, verb, target):
    Notification.objects.create(
        recipient=recipient,
        actor=actor,
        verb=verb,
        content_type=ContentType.objects.get_for_model(target),
        object_id=target.id
    )
