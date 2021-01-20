import pytest

from unittest.mock import patch

from django.conf import settings
from django.test import TestCase
from django.utils import timezone

from chat.models import Thread, Message
from chat.tests.factories import ThreadFactory, MessageFactory
from users.tests.factories import UserFactory


pytestmark = pytest.mark.django_db


class ThreadModelTestCase(TestCase):
    def setUp(self):
        self.first_user = UserFactory()
        self.second_user = UserFactory()
        self.participants = ThreadFactory.create(
            participants=(self.first_user, self.second_user)
        )

    def test_thread(self):
        self.assertEqual(self.participants.pk, 1)