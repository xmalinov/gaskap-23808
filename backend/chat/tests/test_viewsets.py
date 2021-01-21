import factory

from django.urls import reverse
from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from rest_framework.authtoken.models import Token

from chat.tests.factories import ThreadFactory, MessageFactory
from users.tests.factories import UserFactory

User = get_user_model()


class MessageAPIViewTestCase(APITestCase):
    def setUp(self):
        self.user = UserFactory()
        self.teacher_user = UserFactory(user_type=User.USER_TYPE_TEACHER)
        self.user_pass = factory.Faker("password")
        self.user.set_password(self.user_pass)
        self.user.save()

        self.client = APIClient()

        token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {token}")
        self.thread = ThreadFactory.create(
            participants=(self.user.id, self.teacher_user.id)
        )

        self.message = MessageFactory.create(thread=self.thread, contact=self.user)

    def test_create_thread(self):
        data = {"participants": [self.user.id, self.teacher_user.id]}
        response = self.client.post(reverse("chat-v1:threads-list"), data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_tread_messages(self):
        response = self.client.get(
            reverse("chat-v1:thread-messages-list", args=(self.thread.id,))
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_thread_message(self):
        response = self.client.get(
            reverse(
                "chat-v1:thread-messages-detail", args=(self.thread.id, self.message.id)
            )
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)