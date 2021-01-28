from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework_extensions.mixins import NestedViewSetMixin
from rest_framework.permissions import IsAuthenticated

from news.api.v1.serializers import NewsSerializer, NewsCommentSerializer
from news.models import News, NewsComment
from news.api.v1.permissions import HasNewsPermissions, HasNewsCommentPermissions

from users.models import User, School


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = [IsAuthenticated, HasNewsPermissions]

    def get_queryset(self):
        qs = super().get_queryset()
        user = self.request.user
        school_filter = {}
        if user.is_student or user.is_teacher:
            school_filter = {"school": user.profile.school}
        elif user.is_parent:
            school_filter = {
                "school__in": user.profile.stident.values_list("school", flat=True)
            }
        else:
            school_filter = {"school": user.profile}

        return qs.filter(**school_filter)

    def perform_create(self, serializer):
        user = self.request.user
        school_id = user.profile.school.id if user.is_teacher else user.profile.id
        school = get_object_or_404(School, pk=school_id)

        serializer.save(school=school, author=self.request.user)


class NewsCommentViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = NewsComment.objects.all()
    serializer_class = NewsCommentSerializer
    permission_classes = [IsAuthenticated, HasNewsCommentPermissions]
    http_method_names = ["post", "get"]

    def perform_create(self, serializer):
        news_instance = get_object_or_404(News, pk=self.kwargs.get("news_pk"))
        serializer.save(news=news_instance, author=self.request.user)
