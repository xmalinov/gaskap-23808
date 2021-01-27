from django.core.files import File
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse

from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase, APIClient

from classes.models import ClassVideo, ClassVideoComment, Class
from classes.tests.factories import (
    ClassFactory,
    ClassVideoFactory,
    ClassVideoCommentFactory,
)
from home.api.v1.tests.test_viewsets import AuthenticatedAPITestCase
from home.tests.factories import WeekDayFactory
from users.models import User
from users.tests.factories import (
    SchoolFactory,
    StudentFactory,
    UserFactory,
    TeacherFactory,
)


class ClassViewSetTestCase(AuthenticatedAPITestCase):
    def setUp(self):
        super().setUp()

        self.user_student = UserFactory(name="student_user")
        self.user_teacher = UserFactory(
            name="teacher_user", user_type=User.USER_TYPE_TEACHER
        )
        self.user_teacher2 = UserFactory(
            name="teacher_user2", user_type=User.USER_TYPE_TEACHER
        )

        self.school_user = UserFactory(
            name="school_user", user_type=User.USER_TYPE_SCHOOL
        )
        self.school_user2 = UserFactory(
            name="school_user2", user_type=User.USER_TYPE_SCHOOL
        )

        self.school = SchoolFactory(user=self.school_user)
        self.school2 = SchoolFactory(user=self.school_user2)

        self.weekday = WeekDayFactory()
        self.student = StudentFactory(user=self.user_student, school=self.school)
        self.teacher = TeacherFactory(user=self.user_teacher, school=self.school)
        self.teacher2 = TeacherFactory(user=self.user_teacher2, school=self.school)

        self.token = Token.objects.create(user=self.user_teacher)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token.key}")

    def test_create_with_user_from_different_school(self):
        data = {
            "name": "Test name",
            "description": "Test description",
            "start_time": "12:00",
            "end_time": "13:00",
            "days": [self.weekday.id],
            "students": [self.student.id],
            "teacher": self.teacher.id,
        }

        response = self.client.post(reverse("classes-v1:classes-list"), data=data)
        last_class_instance = Class.objects.last()

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(last_class_instance.school, self.school)

    def test_get_class_detail_from_a_different_school(self):
        class_instance = ClassFactory(
            school=self.school2,
            teacher=self.teacher2,
        )

        response = self.client.get(
            reverse("classes-v1:classes-detail", kwargs={"pk": class_instance.id})
        )

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_class_detail(self):
        class_instance = ClassFactory(
            school=self.school,
            teacher=self.teacher,
        )
        ClassFactory(
            school=self.school2,
            teacher=self.teacher2,
        )

        response = self.client.get(
            reverse("classes-v1:classes-detail", kwargs={"pk": class_instance.id})
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get("name"), class_instance.name)
        self.assertEqual(response.data.get("description"), class_instance.description)
        self.assertEqual(response.data.get("school"), class_instance.school.id)


class ClassVideoViewSetTestCase(AuthenticatedAPITestCase):
    def setUp(self):
        super().setUp()

        self.user_teacher = UserFactory(
            name="user_teacher", user_type=User.USER_TYPE_TEACHER
        )
        self.user_school = UserFactory(
            name="user_school", user_type=User.USER_TYPE_SCHOOL
        )
        self.user_school2 = UserFactory(
            name="user_school2", user_type=User.USER_TYPE_SCHOOL
        )

        self.school = SchoolFactory(
            user=self.user_school, student_code="Sj8bl", teacher_code="TeF61"
        )
        self.school2 = SchoolFactory(
            user=self.user_school2, student_code="Sj8bk", teacher_code="TeF65"
        )

        self.teacher = TeacherFactory(school=self.school, user=self.user_teacher)

        self.class_record = ClassFactory(school=self.school, teacher=self.teacher)

        self.user_teacher2 = UserFactory(
            name="user_teacher2", user_type=User.USER_TYPE_TEACHER
        )
        self.teacher2 = TeacherFactory(school=self.school2, user=self.user_teacher2)
        self.class_record2 = ClassFactory(
            school=self.school2,
            teacher=self.teacher2,
        )

        self.filename = "test_file"
        self.file = File(open("static/test_file.json", "rb"))
        self.uploaded_file = SimpleUploadedFile(
            self.filename, self.file.read(), content_type="multipart/form-data"
        )

        self.class_video = ClassVideoFactory(
            uploaded_class=self.class_record, author=self.user_teacher
        )
        self.class_video2 = ClassVideoFactory(
            uploaded_class=self.class_record2, author=self.user_teacher
        )

        self.token = Token.objects.create(user=self.user_school)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token.key}")

    def test_get_class_video_detail_from_different_school(self):
        response = self.client.get(
            reverse(
                "classes-v1:class-videos-detail",
                kwargs={
                    "parent_lookup_uploaded_class": self.class_record2.id,
                    "pk": self.class_video.id,
                },
            ),
        )

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_class_video_detail(self):
        response = self.client.get(
            reverse(
                "classes-v1:class-videos-detail",
                kwargs={
                    "parent_lookup_uploaded_class": self.class_record.id,
                    "pk": self.class_video.id,
                },
            ),
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get("description"), self.class_video.description)
        self.assertEqual(
            response.data.get("uploaded_class"), self.class_video.uploaded_class.id
        )
        self.assertEqual(
            response.data.get("author")["email"], self.class_video.author.email
        )

    def test_create_class_video_with_invalid_class_id(self):
        data = {
            "name": "Test Name",
            "description": "Test Description",
            "video": self.uploaded_file,
            "uploaded_class": self.class_record.id,
            "author": self.user.id,
        }

        response = self.client.post(
            reverse(
                "classes-v1:class-videos-list",
                kwargs={"parent_lookup_uploaded_class": 9999},
            ),
            data=data,
        )

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_class_video_for_a_class_in_a_different_school(self):
        data = {
            "name": "Test Name",
            "description": "Test Description",
            "video": self.uploaded_file,
            "uploaded_class": self.class_record2.id,
        }

        response = self.client.post(
            reverse(
                "classes-v1:class-videos-list",
                kwargs={"parent_lookup_uploaded_class": self.class_record2.id},
            ),
            data=data,
        )

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_class_video(self):
        data = {
            "name": "Test Name",
            "description": "Test Description",
            "video": self.uploaded_file,
            "uploaded_class": self.class_record.id,
        }

        response = self.client.post(
            reverse(
                "classes-v1:class-videos-list",
                kwargs={"parent_lookup_uploaded_class": self.class_record.id},
            ),
            data=data,
        )

        class_video = ClassVideo.objects.last()

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(class_video.uploaded_class.id, data.get("uploaded_class"))
        self.assertEqual(class_video.author, self.user_school)


class ClassVideoCommentViewSetTestCase(AuthenticatedAPITestCase):
    def setUp(self):
        super().setUp()
        self.user_school = UserFactory(
            name="user_school", user_type=User.USER_TYPE_SCHOOL
        )
        self.user_school2 = UserFactory(
            name="user_school", user_type=User.USER_TYPE_SCHOOL
        )
        self.user_teacher = UserFactory(
            name="user_teacher", user_type=User.USER_TYPE_TEACHER
        )
        self.user_teacher2 = UserFactory(
            name="user_teacher2", user_type=User.USER_TYPE_TEACHER
        )

        self.school = SchoolFactory(user=self.user_school)
        self.teacher = TeacherFactory(school=self.school, user=self.user_teacher)

        self.class_instance = ClassFactory(school=self.school, teacher=self.teacher)
        self.class_video = ClassVideoFactory(
            author=self.user_teacher, uploaded_class=self.class_instance
        )
        self.class_video_comment = ClassVideoCommentFactory(
            video=self.class_video, author=self.user_teacher
        )

        self.school2 = SchoolFactory(user=self.user_school2)
        self.teacher2 = TeacherFactory(school=self.school2, user=self.user_teacher2)

        self.class_instance2 = ClassFactory(school=self.school2, teacher=self.teacher2)
        self.class_video2 = ClassVideoFactory(
            author=self.user_teacher2, uploaded_class=self.class_instance2
        )
        self.class_video_comment2 = ClassVideoCommentFactory(
            video=self.class_video2, author=self.user_teacher2
        )

        self.token = Token.objects.create(user=self.user_teacher)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token.key}")

    def test_get_class_video_comment_detail_for_a_class_in_a_different_school(self):
        response = self.client.get(
            reverse(
                "classes-v1:class-video-comments-detail",
                kwargs={
                    "parent_lookup_video__uploaded_class": self.class_video2.uploaded_class.id,
                    "parent_lookup_video": self.class_video2.id,
                    "pk": self.class_video_comment.id,
                },
            ),
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_class_video_comment_detail(self):
        response = self.client.get(
            reverse(
                "classes-v1:class-video-comments-detail",
                kwargs={
                    "parent_lookup_video__uploaded_class": self.class_video.uploaded_class.id,
                    "parent_lookup_video": self.class_video.id,
                    "pk": self.class_video_comment.id,
                },
            ),
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_class_video_comment_for_a_class_in_a_different_school(self):
        data = {
            "content": "Test content",
            "video": self.class_video.id,
        }

        response = self.client.post(
            reverse(
                "classes-v1:class-video-comments-list",
                kwargs={
                    "parent_lookup_video__uploaded_class": self.class_video2.uploaded_class.id,
                    "parent_lookup_video": self.class_video2.id,
                },
            ),
            data=data,
        )

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_class_video_comment_with_invalid_class_id(self):
        data = {
            "content": "Test content",
        }

        response = self.client.post(
            reverse(
                "classes-v1:class-video-comments-list",
                kwargs={
                    "parent_lookup_video__uploaded_class": 9999,
                    "parent_lookup_video": self.class_video.id,
                },
            ),
            data=data,
        )

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_class_video_comment_with_invalid_video_id(self):
        data = {
            "content": "Test content",
        }

        response = self.client.post(
            reverse(
                "classes-v1:class-video-comments-list",
                kwargs={
                    "parent_lookup_video__uploaded_class": self.class_video.uploaded_class.id,
                    "parent_lookup_video": 9999,
                },
            ),
            data=data,
        )

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_class_video_comment(self):
        data = {
            "content": "Test content",
            "video": self.class_video.id,
        }

        response = self.client.post(
            reverse(
                "classes-v1:class-video-comments-list",
                kwargs={
                    "parent_lookup_video__uploaded_class": self.class_video.uploaded_class.id,
                    "parent_lookup_video": self.class_video.id,
                },
            ),
            data=data,
        )

        video_comment = ClassVideoComment.objects.last()

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(video_comment.video.id, data.get("video"))
        self.assertEqual(video_comment.content, data.get("content"))


class ClassStudentViewSetTestCase(AuthenticatedAPITestCase):
    def setUp(self):
        self.user_student = UserFactory(name="user_student")
        self.user_student2 = UserFactory(name="user_student2")

        self.user_teacher = UserFactory(
            name="teacher_user", user_type=User.USER_TYPE_TEACHER
        )
        self.user_teacher2 = UserFactory(
            name="teacher_user2", user_type=User.USER_TYPE_TEACHER
        )

        self.school_user = UserFactory(
            name="school_user", user_type=User.USER_TYPE_SCHOOL
        )
        self.school_user2 = UserFactory(
            name="school_user2", user_type=User.USER_TYPE_SCHOOL
        )

        self.school = SchoolFactory(user=self.school_user)
        self.student = StudentFactory(user=self.user_student, school=self.school)
        self.teacher = TeacherFactory(user=self.user_teacher, school=self.school)

        self.class_instance = ClassFactory(school=self.school, teacher=self.teacher)
        self.class_instance.students.add(self.student)

        self.school2 = SchoolFactory(user=self.school_user2)
        self.student2 = StudentFactory(user=self.user_student2, school=self.school2)

        self.teacher2 = TeacherFactory(user=self.user_teacher2, school=self.school2)

        self.class_instance2 = ClassFactory(school=self.school2, teacher=self.teacher2)
        self.class_instance2.students.add(self.student2)

        self.token = Token.objects.create(user=self.user_student)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token.key}")

    def test_get_class_students_from_another_school(self):
        response = self.client.get(
            reverse(
                "classes-v1:class-students-detail",
                kwargs={
                    "parent_lookup_student__classes": self.class_instance2.id,
                    "pk": self.user_student2.id,
                },
            )
        )

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_class_students(self):
        response = self.client.get(
            reverse(
                "classes-v1:class-students-detail",
                kwargs={
                    "parent_lookup_student__classes": self.class_instance.id,
                    "pk": self.user_student.id,
                },
            )
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get("email"), self.user_student.email)
        self.assertEqual(response.data.get("name"), self.user_student.name)
        self.assertEqual(response.data.get("user_type"), self.user_student.user_type)
        self.assertEqual(
            response.data.get("profile").get("student_id"),
            self.user_student.student.student_id,
        )
