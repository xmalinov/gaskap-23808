from django.test import TestCase, RequestFactory

from home.api.v1.serializers import (
    SignupSerializer,
    StudentSerializer,
    TeacherSerializer,
    ParentSerializer,
    SchoolSerializer,
    UserSerializer,
)
from users.tests.factories import (
    UserFactory,
    SchoolFactory,
    StudentFactory,
    ParentFactory,
    TeacherFactory,
)
from users.models import User, School, Student, Teacher, Parent


class SignupSerializerTestCase(TestCase):
    def setUp(self):
        self.user = UserFactory()

        self.request = RequestFactory().get("./fake_path")
        self.request.session = self.client.session
        self.request.user = self.user

        self.school = SchoolFactory(user=self.user)

    def test_create_user_with_invalid_phone_number(self):
        data = {
            "name": "John Doe",
            "email": "john_doe@example.com",
            "phone_number": "abcjjdjsaj",
            "password": "johndoe123",
            "code": self.school.student_code,
            "user_type": "student",
        }

        serializer = SignupSerializer(data=data, context={"request": self.request})
        self.assertFalse(serializer.is_valid())

    def test_create_user_with_invalid_user_type(self):
        data = {
            "name": "John Doe",
            "email": "john_doe@example.com",
            "phone_number": "+639958871292",
            "password": "johndoe123",
            "code": self.school.student_code,
            "user_type": "school",
        }

        serializer = SignupSerializer(data=data, context={"request": self.request})
        self.assertFalse(serializer.is_valid())

    def test_create_user_with_invalid_code(self):
        data = {
            "name": "John Doe",
            "email": "john_doe@example.com",
            "phone_number": "+639958871292",
            "password": "johndoe123",
            "code": "random code",
            "user_type": "student",
        }

        serializer = SignupSerializer(data=data, context={"request": self.request})
        self.assertFalse(serializer.is_valid())

    def test_create_user_with_duplicate_email(self):
        data = {
            "name": "John Doe",
            "email": self.user.email,
            "phone_number": "+639958871292",
            "password": "johndoe123",
            "code": self.school.student_code,
            "user_type": "student",
        }

        serializer = SignupSerializer(data=data, context={"request": self.request})
        self.assertFalse(serializer.is_valid())

    def test_create_student_user(self):
        data = {
            "name": "John Doe",
            "email": "john_doe@example.com",
            "phone_number": "+639958871292",
            "password": "johndoe123",
            "code": self.school.student_code,
            "user_type": "student",
        }

        user_count = User.objects.count()
        student_count = Student.objects.count()

        serializer = SignupSerializer(data=data, context={"request": self.request})
        self.assertTrue(serializer.is_valid())

        instance = serializer.save()
        student = Student.objects.last()

        self.assertEqual(User.objects.count(), user_count + 1)
        self.assertEqual(Student.objects.count(), student_count + 1)
        self.assertEqual(instance.name, data.get("name"))
        self.assertEqual(instance.email, data.get("email"))
        self.assertEqual(student.phone_number, data.get("phone_number"))
        self.assertEqual(student.school.student_code, data.get("code"))
        self.assertEqual(instance.user_type, data.get("user_type"))

    def test_create_parent_user(self):
        student = StudentFactory(school=self.school)
        data = {
            "name": "John Doe",
            "email": "john_doe@example.com",
            "phone_number": "+639958871292",
            "password": "johndoe123",
            "code": student.student_id,
            "user_type": "parent",
        }

        user_count = User.objects.count()
        parent_count = Parent.objects.count()

        serializer = SignupSerializer(data=data, context={"request": self.request})
        self.assertTrue(serializer.is_valid())

        instance = serializer.save()
        parent = Parent.objects.last()

        self.assertEqual(User.objects.count(), user_count + 1)
        self.assertEqual(Parent.objects.count(), parent_count + 1)
        self.assertEqual(instance.name, data.get("name"))
        self.assertEqual(instance.email, data.get("email"))
        self.assertEqual(parent.phone_number, data.get("phone_number"))
        self.assertEqual(parent.students.first().student_id, data.get("code"))
        self.assertEqual(instance.user_type, data.get("user_type"))

    def test_create_teacher_user(self):
        data = {
            "name": "John Doe",
            "email": "john_doe@example.com",
            "phone_number": "+639958871292",
            "password": "johndoe123",
            "code": self.school.teacher_code,
            "user_type": "teacher",
        }

        user_count = User.objects.count()
        teacher_count = Teacher.objects.count()

        serializer = SignupSerializer(data=data, context={"request": self.request})
        self.assertTrue(serializer.is_valid())

        instance = serializer.save()
        teacher = Teacher.objects.last()

        self.assertEqual(User.objects.count(), user_count + 1)
        self.assertEqual(Teacher.objects.count(), teacher_count + 1)
        self.assertEqual(instance.name, data.get("name"))
        self.assertEqual(instance.email, data.get("email"))
        self.assertEqual(teacher.phone_number, data.get("phone_number"))
        self.assertEqual(teacher.school.teacher_code, data.get("code"))
        self.assertEqual(instance.user_type, data.get("user_type"))


class StudentSerializerTestCase(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.school = SchoolFactory(user=self.user)
        self.student = StudentFactory(school=self.school)

    def test_update_with_invalid_phone_number(self):
        data = {
            "phone_number": "123456",
            "state": "Texas",
            "city": "Dallas",
            "student_id": "string",
            "grade": "kindergarten",
            "date_of_birth": "2021-01-15",
        }

        serializer = StudentSerializer(data=data, instance=self.student)
        self.assertFalse(serializer.is_valid())

    def test_update(self):
        data = {
            "phone_number": "+639958871292",
            "state": "Texas",
            "city": "Dallas",
            "student_id": "string",
            "grade": "kindergarten",
            "date_of_birth": "2021-01-15",
        }

        serializer = StudentSerializer(data=data, instance=self.student)
        self.assertTrue(serializer.is_valid())

        serializer.save()

        self.assertEqual(serializer.data.get("phone_number"), data.get("phone_number"))
        self.assertEqual(serializer.data.get("state"), data.get("state"))
        self.assertEqual(serializer.data.get("city"), data.get("city"))
        self.assertEqual(serializer.data.get("grade"), data.get("grade"))
        self.assertEqual(
            serializer.data.get("date_of_birth"), data.get("date_of_birth")
        )


class SchoolSerializerTestCase(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.school = SchoolFactory(user=self.user)

    def test_update_with_invalid_phone_number(self):
        data = {
            "number": "123",
            "phone_number": "12345",
            "state": "California",
            "city": "Sacramento",
            "color": "#FFFFFF",
        }

        serializer = SchoolSerializer(data=data, instance=self.school)

        self.assertFalse(serializer.is_valid())

    def test_update(self):
        data = {
            "number": "123",
            "phone_number": "+639958871292",
            "state": "California",
            "city": "Sacramento",
            "color": "#FFFFFF",
        }

        serializer = SchoolSerializer(data=data, instance=self.school)

        self.assertTrue(serializer.is_valid())

        serializer.save()

        self.assertEqual(serializer.data.get("phone_number"), data.get("phone_number"))
        self.assertEqual(serializer.data.get("state"), data.get("state"))
        self.assertEqual(serializer.data.get("city"), data.get("city"))
        self.assertEqual(serializer.data.get("color"), data.get("color"))
        self.assertEqual(serializer.data.get("number"), data.get("number"))


class ParentSerializerTestCase(TestCase):
    def setUp(self):
        self.user = UserFactory()

        self.school = SchoolFactory(user=self.user)
        self.student = StudentFactory(school=self.school)

        self.parent = ParentFactory()
        self.parent.students.add(self.student)
        self.parent.save()

    def test_update_with_invalid_phone_number(self):
        data = {
            "phone_number": "123456",
            "state": "California",
            "city": "Sacramento",
            "date_of_birth": "2021-01-01",
        }

        serializer = ParentSerializer(data=data, instance=self.parent)
        self.assertFalse(serializer.is_valid())

    def test_update(self):
        data = {
            "phone_number": "+639958871292",
            "state": "California",
            "city": "Sacramento",
            "date_of_birth": "2021-01-01",
        }

        serializer = ParentSerializer(data=data, instance=self.parent)
        self.assertTrue(serializer.is_valid())

        serializer.save()

        self.assertEqual(serializer.data.get("phone_number"), data.get("phone_number"))
        self.assertEqual(serializer.data.get("state"), data.get("state"))
        self.assertEqual(serializer.data.get("city"), data.get("city"))
        self.assertEqual(
            serializer.data.get("date_of_birth"), data.get("date_of_birth")
        )


class TeacherSerializerTestCase(TestCase):
    def setUp(self):
        self.user = UserFactory()

        self.school = SchoolFactory(user=self.user)
        self.teacher = TeacherFactory(school=self.school)

    def test_update_with_invalid_phone_number(self):
        data = {
            "phone_number": "123456",
            "state": "California",
            "city": "Sacramento",
            "date_of_birth": "2021-01-01",
            "subject": "Science",
        }

        serializer = TeacherSerializer(data=data, instance=self.teacher)
        self.assertFalse(serializer.is_valid())

    def test_update(self):
        data = {
            "phone_number": "+639958871292",
            "state": "California",
            "city": "Sacramento",
            "date_of_birth": "2021-01-01",
            "subject": "Science",
        }

        serializer = TeacherSerializer(data=data, instance=self.teacher)
        self.assertTrue(serializer.is_valid())

        serializer.save()

        self.assertEqual(serializer.data.get("phone_number"), data.get("phone_number"))
        self.assertEqual(serializer.data.get("state"), data.get("state"))
        self.assertEqual(serializer.data.get("city"), data.get("city"))
        self.assertEqual(
            serializer.data.get("date_of_birth"), data.get("date_of_birth")
        )
        self.assertEqual(serializer.data.get("subject"), data.get("subject"))


class UserSerializerTestCase(TestCase):
    def setUp(self):
        self.user = UserFactory()

        self.request = RequestFactory().get("./fake_path")
        self.request.user = self.user
        self.request.session = self.client.session

        self.school = SchoolFactory()
        self.student = StudentFactory(user=self.user, school=self.school)

    def test_update(self):
        data = {"email": "user@example.com", "name": "string", "is_active": False}

        serializer = UserSerializer(
            data=data, context={"request": self.request}, instance=self.user
        )
        self.assertTrue(serializer.is_valid())

        serializer.save()

        self.assertEqual(serializer.data.get("email"), data.get("email"))
        self.assertEqual(serializer.data.get("name"), data.get("name"))
        self.assertEqual(serializer.data.get("is_active"), data.get("is_active"))
