# Check if fields are not null
from django.test import TestCase

from users.models import User
from users.tests.factories import UserFactory, SchoolFactory, StudentFactory


class SchoolSignalTestCase(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.school = SchoolFactory()

    def test_student_code(self):
        self.assertIsNotNone(self.school.student_code)

    def test_teacher_code(self):
        self.assertIsNotNone(self.school.teacher_code)


class StudentIDSignalTestCase(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.school = SchoolFactory()
        self.student = StudentFactory(school=self.school)

    def test_student_id(self):
        self.assertIsNotNone(self.student.student_id)
