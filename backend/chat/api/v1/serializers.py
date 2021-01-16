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
    class Meta:
        model = Thread
        fields = (
            "id",
            "participants",
        )
