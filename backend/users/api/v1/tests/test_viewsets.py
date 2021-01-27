import factory

from django.urls import reverse

from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase, APIClient
from unittest.mock import patch

from home.api.v1.tests.test_viewsets import AuthenticatedAPITestCase
from users.tests.factories import (
    UserFactory,
    EmailAddressFactory,
    SchoolFactory,
    StudentFactory,
    ParentFactory,
    TeacherFactory,
)
from users.api.v1.tests.mocks import mock_send_confirmation


class ProfileAPIViewTestCase(AuthenticatedAPITestCase):
    def setUp(self):
        super().setUp()
        self.school = SchoolFactory()
        self.student = StudentFactory(user=self.user, school=self.school)

    def test_update_student(self):
        data = {
            "phone_number": "+639957651273",
            "state": "string",
            "city": "string",
            "student_id": "string",
            "grade": "kindergarten",
            "date_of_birth": "2021-01-19",
        }
        response = self.client.patch(reverse("users-v1:profile_edit"), data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_student_with_invalid_phone_number(self):
        data = {"phone_number": "123456", "state": "string", "city": "string"}

        response = self.client.patch(reverse("users-v1:profile_edit"), data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class EmailConfirmationViewsetTestCase(APITestCase):
    def setUp(self):
        self.user = UserFactory()
        self.email = EmailAddressFactory(email=self.user.email)

    @patch(
        "users.api.v1.viewsets.EmailAddress.send_confirmation",
        side_effect=mock_send_confirmation,
    )
    def test_send_email_confirmation(self, mock_send_confirmation):
        data = {"email": self.user.email}
        response = self.client.post(
            reverse("users-v1:send-email-confirmation"), data=data
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        mock_send_confirmation.assert_called_once()

    def test_send_email_already_verified(self):
        self.email.verified = True
        self.email.save()

        data = {"email": self.user.email}
        response = self.client.post(
            reverse("users-v1:send-email-confirmation"), data=data
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_send_email_confirmation_unexisting_email(self):
        data = {"email": "john_doe@example.com"}
        response = self.client.post(
            reverse("users-v1:send-email-confirmation"), data=data
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class UsersListViewSetTestCase(AuthenticatedAPITestCase):
    def setUp(self):
        super().setUp()
        self.school_user = UserFactory(user_type="school")
        self.school = SchoolFactory(user=self.school_user)

    def test_get_users_list_without_school(self):
        response = self.client.get(reverse("users-v1:users-list"))

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_users_list(self):
        response = self.client.get(
            reverse("users-v1:users-list"), {"school": self.school.id}
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
