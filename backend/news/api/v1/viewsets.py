from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework_extensions.mixins import NestedViewSetMixin
from rest_framework.permissions import IsAuthenticated

from news.api.v1.serializers import NewsSerializer, NewsCommentSerializer
from news.models import News, NewsComment
from news.api.v1.permissions import HasNewsPermissions, HasNewsCommentPermissions


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = [IsAuthenticated, HasNewsPermissions]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class NewsCommentViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = NewsComment.objects.all()
    serializer_class = NewsCommentSerializer
    permission_classes = [IsAuthenticated, HasNewsCommentPermissions]
    http_method_names = ["post", "get"]

    def perform_create(self, serializer):
        news_instance = get_object_or_404(News, pk=self.kwargs.get("news_pk"))
        serializer.save(news=news_instance, author=self.request.user)
