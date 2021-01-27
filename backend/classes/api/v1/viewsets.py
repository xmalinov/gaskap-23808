from django.db.models import Q
from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework_extensions.mixins import NestedViewSetMixin
from rest_framework.permissions import IsAuthenticated

from classes.api.v1.permissions import (
    HasClassPermission,
    HasClassVideoPermission,
    HasClassVideoCommentPermission,
)
from classes.api.v1.serializers import (
    ClassVideoCommentSerializer,
    ClassVideoSerializer,
    ClassSerializer,
)
from classes.models import ClassVideoComment, ClassVideo, Class
from users.api.v1.serializers import UserSerializer
from users.models import User, School


class ClassVideoCommentViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    serializer_class = ClassVideoCommentSerializer
    queryset = ClassVideoComment.objects.all()
    permission_classes = [IsAuthenticated, HasClassVideoCommentPermission]

    def get_queryset(self):
        qs = super().get_queryset()
        user = self.request.user

        school_filter = {}
        if user.is_student or user.is_teacher:
            school_filter = {"video__uploaded_class__school": user.profile.school}
        elif user.is_parent:
            school_filter = {
                "video__uploaded_class__school__in": user.profile.students.values_list(
                    "school", flat=True
                )
            }
        else:
            school_filter = {"video__uploaded_class__school": user.profile}
        return qs.filter(**school_filter)

    def perform_create(self, serializer):
        user = self.request.user
        school = user.profile.school if user.is_teacher else user.profile
        video = get_object_or_404(
            ClassVideo,
            pk=self.kwargs.get("parent_lookup_video"),
            uploaded_class_id=self.kwargs.get("parent_lookup_video__uploaded_class"),
            uploaded_class__school=school,
        )
        serializer.save(video=video, author=self.request.user)


class ClassVideoViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    serializer_class = ClassVideoSerializer
    queryset = ClassVideo.objects.all()
    permission_classes = [IsAuthenticated, HasClassVideoPermission]

    def get_queryset(self):
        qs = super().get_queryset()
        user = self.request.user

        school_filter = {}
        if user.is_student or user.is_teacher:
            school_filter = {"uploaded_class__school": user.profile.school}
        elif user.is_parent:
            school_filter = {
                "uploaded_class__school__in": user.profile.students.values_list(
                    "school", flat=True
                )
            }
        else:
            school_filter = {"uploaded_class__school": user.profile}

        return qs.filter(**school_filter)

    def perform_create(self, serializer):
        user = self.request.user
        school = user.profile.school if user.is_teacher else user.profile
        class_instance = get_object_or_404(
            Class, pk=self.kwargs.get("parent_lookup_uploaded_class"), school=school
        )

        serializer.save(uploaded_class=class_instance, author=self.request.user)


class ClassViewSet(viewsets.ModelViewSet):
    serializer_class = ClassSerializer
    queryset = Class.objects.all()
    permission_classes = [IsAuthenticated, HasClassPermission]

    def get_queryset(self):
        qs = super().get_queryset()
        user = self.request.user
        school_filter = {}
        if user.is_student or user.is_teacher:
            school_filter = {"school": user.profile.school}
        elif user.is_parent:
            school_filter = {
                "school__in": user.profile.students.values_list("school", flat=True)
            }
        else:
            school_filter = {"school": user.profile}

        return qs.filter(**school_filter)

    def perform_create(self, serializer):
        """Only teacher and school user types will be able
        to create classes"""
        user = self.request.user
        school_id = user.profile.school.id if user.is_teacher else user.profile.id
        school = get_object_or_404(School, pk=school_id)

        serializer.save(school=school)


class ClassStudentViewSet(NestedViewSetMixin, viewsets.ReadOnlyModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.active()

    def get_queryset(self):
        qs = super().get_queryset()
        user = self.request.user

        school_filter = {}
        if user.is_student:
            school_filter = {"student__classes__school": user.student.school}
        elif user.is_parent:
            school_filter = {
                "student__classes__school__in": user.parent.students.values_list(
                    "school", flat=True
                )
            }
        elif user.is_teacher:
            school_filter = {"student__classes__school": user.teacher.school}
        else:
            school_filter = {"student__classes__school": user.school}
        return qs.filter(**school_filter).distinct()
