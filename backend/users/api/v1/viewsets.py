from allauth.account.models import EmailAddress
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, viewsets
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.generics import UpdateAPIView, GenericAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from users.api.v1.serializers import (
    EmailResetSerializer,
    ParentSerializer,
    SchoolSerializer,
    StudentSerializer,
    TeacherSerializer,
    UserSerializer,
)
from users.models import User
from users.filters import UserFilter


class ProfileAPIView(UpdateAPIView):
    """Update profile of user depending on user type"""

    def get_object(self):
        if self.request.user.user_type == User.USER_TYPE_SCHOOL:
            return self.request.user.school
        elif self.request.user.user_type == User.USER_TYPE_PARENT:
            return self.request.user.parent
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


class EmailConfirmation(GenericAPIView):
    """Resend email verification"""

    serializer_class = EmailResetSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        email_addresses = EmailAddress.objects.filter(email=request.data.get("email"))
        if not email_addresses.exists():
            return Response(
                {"message": "Email does not exist."}, status=status.HTTP_400_BAD_REQUEST
            )

        email_address = email_addresses.first()
        if email_address.verified:
            return Response(
                {"message": "Email already verified"},
                status=status.HTTP_200_OK,
            )

        email_address.send_confirmation(request=request, signup=False)
        return Response(
            {"message": "Email confirmation sent"}, status=status.HTTP_200_OK
        )


class UsersListViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all().distinct()
    filter_backends = [DjangoFilterBackend]
    filterset_class = UserFilter
