import json
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.http import HttpResponseForbidden
from django.utils.encoding import force_text
from django.utils.translation import ugettext as _
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer


from .models import Message, Thread


User = get_user_model()


class ChatConsumer(WebsocketConsumer):
    def new_message(self, data):
        thread = Thread.objects.filter(
            id=self.thread_id, participants=self.user
        ).first()
        if not thread:
            message = "You are not authorized to send a message to this thread"
            raise ValidationError(message)
        message = Message.objects.create(
            contact=self.user, content=data["message"], thread=thread
        )
        content = {"command": "new_message", "message": self.message_to_json(message)}

        return self.send_chat_message(content)

    def messages_to_json(self, messages):
        return [self.message_to_json(message) for message in messages]

    def message_to_json(self, message):
        return {
            "id": message.id,
            "author": message.contact.id,
            "content": message.content,
            "timestamp": str(message.created),
        }

    commands = {"new_message": new_message}

    def connect(self):
        self.thread_id = self.scope["url_route"]["kwargs"]["thread_id"]
        self.thread_group = f"thread_{self.thread_id}"
        self.user = self.scope["user"]
        async_to_sync(self.channel_layer.group_add)(
            self.thread_group, self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.thread_group, self.channel_name
        )

    def receive(self, text_data):
        data = json.loads(text_data)
        self.commands[data["command"]](self, data)

    def send_chat_message(self, message):
        async_to_sync(self.channel_layer.group_send)(
            self.thread_group, {"type": "chat_message", "message": message}
        )

    def send_message(self, message):
        self.send(text_data=json.dumps(message))

    def chat_message(self, event):
        message = event["message"]
        self.send(text_data=json.dumps(message))
