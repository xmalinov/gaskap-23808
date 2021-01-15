from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import serializers

from chat.models import Thread


class ParticipantSerializer(serializers.StringRelatedField):
    def to_internal_value(self, value):
        return value


User = get_user_model()


class ThreadSerializer(serializers.ModelSerializer):
    participants = ParticipantSerializer(many=True)

    class Meta:
        model = Thread
        fields = ("id", "messages", "participants")

    def create(self, validated_data):
        participants = validated_data.get("participants", None)
        thread = Thread()
        thread.save()
        for username in participants:
            user = get_object_or_404(User, username=username)
            thread.participants.add(user)
        thread.save()
        return thread
