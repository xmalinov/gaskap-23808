from django.db.models import Q
from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework_extensions.mixins import NestedViewSetMixin
from rest_framework.permissions import IsAuthenticated

from classes.api.v1.permissions import HasClassPermission
from classes.api.v1.serializers import (
    ClassVideoCommentSerializer,
    ClassVideoSerializer,
    ClassSerializer,
)
from classes.models import ClassVideoComment, ClassVideo, Class
from users.api.v1.serializers import UserSerializer
from users.models import User


class ClassVideoCommentViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    serializer_class = ClassVideoCommentSerializer
    queryset = ClassVideoComment.objects.all()

    def perform_create(self, serializer):
        video = get_object_or_404(
            ClassVideo,
            pk=self.kwargs.get("parent_lookup_video"),
            uploaded_class_id=self.kwargs.get("parent_lookup_video__uploaded_class"),
        )
        serializer.save(video=video, author=self.request.user)


class ClassVideoViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    serializer_class = ClassVideoSerializer
    queryset = ClassVideo.objects.all()

    def perform_create(self, serializer):
        class_instance = get_object_or_404(
            Class, pk=self.kwargs.get("parent_lookup_uploaded_class")
        )
        serializer.save(uploaded_class=class_instance, author=self.request.user)


class ClassViewSet(viewsets.ModelViewSet):
    serializer_class = ClassSerializer
    queryset = Class.objects.all()
    permission_classes = [IsAuthenticated, HasClassPermission]

    def get_queryset(self):
        qs = super().get_queryset()
        user = self.request.user
        student_teacher_list = ["student", "teacher"]

        if user.user_type in student_teacher_list:
            return qs.filter(teacher__school=user.profile.school)
        elif user.user_type == "parent":
            return qs.filter(teacher__school=user.profile.students.first().school)
        return qs.filter(teacher__school=user.profile)


class ClassStudentViewSet(NestedViewSetMixin, viewsets.ReadOnlyModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
