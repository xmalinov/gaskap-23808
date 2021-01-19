from rest_framework import status
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import UpdateAPIView

from home.api.v1.serializers import (
    StudentSerializer,
    ParentSerializer,
    TeacherSerializer,
    SchoolSerializer,
)
from users.models import User


class ProfileAPIView(UpdateAPIView):
    """Update profile of user depending on user type"""

    def get_object(self):
        if self.request.user.user_type == User.USER_TYPE_SCHOOL:
            return self.request.user.school
        elif self.request.user.user_type == User.USER_TYPE_PARENT:
            return self.request.user.teacher
        elif self.request.user.user_type == User.USER_TYPE_TEACHER:
            return self.request.user.teacher
        else:
            return self.request.user.student

    def get_serializer_class(self):
        if self.request.user.user_type == User.USER_TYPE_SCHOOL:
            return SchoolSerializer
        elif self.request.user.user_type == User.USER_TYPE_PARENT:
            return ParentSerializer
        elif self.request.user.user_type == User.USER_TYPE_TEACHER:
            return TeacherSerializer
        else:
            return StudentSerializer
