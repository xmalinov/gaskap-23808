from rest_framework import serializers

from home.models import WeekDay


class WeekDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = WeekDay
        fields = ["id", "name"]
