import factory

from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from users.tests.factories import (
    UserFactory,
    EmailAddressFactory,
    SchoolFactory,
    StudentFactory,
    ParentFactory,
    TeacherFactory,
)


class ProfileAPIViewTestCase(APITestCase):
    def setUp(self):
        self.user = UserFactory()
        self.user_pass = factory.Faker("password")
        self.user.set_password(self.user_pass)
        self.user.save()

        self.client = APIClient()
        self.client.login(username=self.user.username, password=self.user_pass)

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
