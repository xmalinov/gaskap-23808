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
    def isAuthorized(self):
        authorization = True
        user_contact = get_object_or_404(User, username=self.me)
        chat_participants = User.objects.filter(threads__id=self.room_name)
        if user_contact not in chat_participants:
            authorization = False
        return authorization

    def fetch_messages(self, data):
        if not self.isAuthorized():
            message = "You are not authorized to view messages in this chat"
            raise ValidationError(message)

        messages = Thread.get_last_10_messages(self.room_name)
        content = {"messages": self.messages_to_json(messages)}

        self.send_message(content)

    def new_message(self, data):
        if not self.isAuthorized():
            message = "You are not authorized to send a message to this chat"
            raise ValidationError(message)

        user_contact = get_object_or_404(User, username=self.me)
        message = Message.objects.create(contact=user_contact, content=data["message"])
        current_chat = get_object_or_404(Thread, id=self.room_name)
        current_chat.messages.add(message)
        content = {"command": "new_message", "message": self.message_to_json(message)}

        return self.send_chat_message(content)

    def messages_to_json(self, messages):
        return [self.message_to_json(message) for message in messages]

    def message_to_json(self, message):
        return {
            "id": message.id,
            "author": message.contact.username,
            "content": message.content,
            "timestamp": str(message.created),
        }

    commands = {"fetch_messages": fetch_messages, "new_message": new_message}

    def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_name_group = f"chat_{self.room_name}"
        self.me = self.scope["user"]
        async_to_sync(self.channel_layer.group_add)(
            self.room_name_group, self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_name_group, self.channel_name
        )

    def receive(self, text_data):
        data = json.loads(text_data)
        self.commands[data["command"]](self, data)

    def send_chat_message(self, message):
        async_to_sync(self.channel_layer.group_send)(
            self.room_name_group, {"type": "chat_message", "message": message}
        )

    def send_message(self, message):
        self.send(text_data=json.dumps(message))

    def chat_message(self, event):
        message = event["message"]
        self.send(text_data=json.dumps(message))
