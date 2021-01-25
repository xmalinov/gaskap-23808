from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework.exceptions import PermissionDenied

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

    def validate_participants(self, participants):
        user = self.context["request"].user

        if user not in participants:
            raise serializers.ValidationError(
                f"{user.id} should be a participant in this thread."
            )

        if len(participants) != 2:
            raise serializers.ValidationError("A thread should have two users.")

        participant_filter = filter(
            lambda participant: user != participant
            and (
                user.user_type
                and participant.user_type
                in [User.USER_TYPE_STUDENT, User.USER_TYPE_PARENT]
            ),
            participants,
        )
        if list(participant_filter):
            raise PermissionDenied(
                f"You are not authorized to add this user as a participant."
            )

        return participants