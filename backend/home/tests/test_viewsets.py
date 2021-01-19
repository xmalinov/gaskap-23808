import factory

from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from unittest.mock import patch

from home.tests.mocks import mock_send_confirmation
from users.tests.factories import UserFactory, EmailAddressFactory


class EmailConfirmationViewsetTestCase(APITestCase):
    def setUp(self):
        self.user = UserFactory()
        self.user_pass = factory.Faker("password")

        self.user.set_password(self.user_pass)
        self.user.save()

        self.email = EmailAddressFactory(email=self.user.email)

    @patch(
        "home.api.v1.viewsets.EmailAddress.send_confirmation",
        side_effect=mock_send_confirmation,
    )
    def test_send_email_confirmation(self, mock_send_confirmation):
        data = {"email": self.user.email}
        response = self.client.post(
            reverse("home-v1:send-email-confirmation"), data=data
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        mock_send_confirmation.assert_called_once()

    def test_send_email_already_verified(self):
        self.email.verified = True
        self.email.save()

        data = {"email": self.user.email}
        response = self.client.post(
            reverse("home-v1:send-email-confirmation"), data=data
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_send_email_confirmation_unexisting_email(self):
        data = {"email": "john_doe@example.com"}
        response = self.client.post(
            reverse("home-v1:send-email-confirmation"), data=data
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
