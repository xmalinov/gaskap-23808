from django.utils.translation import ugettext_lazy as _

from rest_framework import serializers

from classes.models import Class, ClassVideo, ClassVideoComment
from home.api.v1.serializers import WeekDaySerializer
from users.api.v1.serializers import UserSerializer


class ClassVideoCommentSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = ClassVideoComment
        fields = ["id", "content", "video", "author", "created", "modified"]
        read_only_fields = ["author", "video"]


class ClassVideoSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = ClassVideo
        fields = [
            "id",
            "name",
            "description",
            "uploaded_class",
            "video",
            "author",
            "created",
            "modified",
        ]
        read_only_fields = ["author", "uploaded_class"]


class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = [
            "id",
            "name",
            "description",
            "start_time",
            "end_time",
            "days",
            "students",
            "teacher",
        ]

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["days"] = WeekDaySerializer(instance.days.all(), many=True).data
        data["teacher"] = UserSerializer(instance.teacher.user).data

        return data
