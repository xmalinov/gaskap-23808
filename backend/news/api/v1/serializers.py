from rest_framework import serializers
from news.models import News, NewsComment


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ("id", "author", "school", "headline", "description")
        read_only_fields = ("author", "school")


class NewsCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsComment
        fields = ("id", "author", "news", "comment")
        read_only_fields = ("author", "news")