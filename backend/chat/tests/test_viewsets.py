import factory

from django.urls import reverse
from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from rest_framework.authtoken.models import Token

from chat.tests.factories import ThreadFactory, MessageFactory
from home.api.v1.tests.test_viewsets import AuthenticatedAPITestCase
from users.tests.factories import UserFactory

User = get_user_model()


class MessageAPIViewTestCase(AuthenticatedAPITestCase):
    def setUp(self):
        super().setUp()
        self.teacher_user = UserFactory(user_type=User.USER_TYPE_TEACHER)
        self.parent_user = UserFactory(user_type=User.USER_TYPE_PARENT)
        self.school_user = UserFactory(user_type=User.USER_TYPE_SCHOOL)

        self.thread = ThreadFactory.create(
            participants=(self.user.id, self.teacher_user.id)
        )

        self.message = MessageFactory.create(thread=self.thread, contact=self.user)

    def test_create_thread(self):
        data = {"participants": [self.user.id, self.teacher_user.id]}
        response = self.client.post(reverse("chat-v1:threads-list"), data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_thread_messages(self):
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

    def test_student_cant_add_parent_as_participant(self):
        data = {"participants": [self.user.id, self.parent_user.id]}
        response = self.client.post(reverse("chat-v1:threads-list"), data=data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_thread_should_have_two_participants(self):
        data = {
            "partcipants": [self.user.id, self.teacher_user.id, self.school_user.id]
        }
        response = self.client.post(reverse("chat-v1:threads-list"), data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_thread_user_should_be_a_participant(self):
        """ Thread owner should be a participant """
        data = {"participants": [self.teacher_user.id, self.school_user.id]}
        response = self.client.post(reverse("chat-v1:threads-list"), data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
