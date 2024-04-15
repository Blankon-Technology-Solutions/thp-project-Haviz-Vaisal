from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.db import models
from django.utils import timezone
from django.db.models.signals import post_save, post_delete


from accounts.models import User


class Todo(models.Model):
    """
    This is todo model
    """

    title = models.CharField(max_length=100)
    creator = models.ForeignKey(User, related_name="todos", on_delete=models.CASCADE)
    description = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def _build_message(self, message_type):
        return {
            "type": "recieve_todo",
            "message": {
                "action": message_type,
                "object_type": "todo",
                "data": {
                    "id": str(self.creator.id),
                    "title": self.title,
                    "description": self.description,
                    "created_at": str(self.created_at),
                },
            },
        }

    def _send_message(self, group_name, message):
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(group_name, message)

    @classmethod
    def save_handler(cls, sender, instance, created, **kwargs):
        message = (
            instance._build_message("create")
            if created
            else instance._build_message("update")
        )

        instance._send_message(str(1), message)

    @classmethod
    def delete_handler(cls, sender, instance, *args, **kwargs):
        message = instance._build_message("delete")
        instance._send_message(str(1), message)


post_save.connect(Todo.save_handler, sender=Todo)
post_delete.connect(Todo.delete_handler, sender=Todo)
