from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import serializers

from chat.models import Thread, Message


User = get_user_model()


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ("id", "contact", "content", "thread")


class ThreadSerializer(serializers.ModelSerializer):
    messages = MessageSerializer(many=True)

    class Meta:
        model = Thread
        fields = ("id", "participants", "messages")
        read_only_fields = ("messages",)

    def create(self, validated_data):
        participants = validated_data.get("participants", None)
        thread = Thread()
        thread.save()
        for username in participants:
            user = get_object_or_404(User, username=username)
            thread.participants.add(user)
        return thread
