import pytest

from unittest.mock import patch

from django.conf import settings
from django.test import TestCase
from django.utils import timezone

from users.models import User, Profile
from users.tests.factories import StudentFactory, SchoolFactory, UserFactory

pytestmark = pytest.mark.django_db


class UserModelTestCase(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.school = SchoolFactory()
        self.student = StudentFactory(user=self.user, school=self.school)

    def test_profile(self):
        self.assertEqual(self.user.profile, self.student)

    def test_active_users(self):
        inactive_user = UserFactory(is_active=False)

        self.assertIn(self.user, User.objects.active())
        self.assertNotIn(inactive_user, User.objects.active())


class ProfileModelTestCase(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.school = SchoolFactory()
        self.student = StudentFactory(
            user=self.user,
            school=self.school,
            date_of_birth=timezone.datetime(1994, 2, 5),
        )

    @patch(
        "users.models.timezone.now",
        return_value=timezone.datetime(2020, 1, 1),
    )
    def test_age(self, mock_date_today):
        self.assertEqual(25, self.student.age)
