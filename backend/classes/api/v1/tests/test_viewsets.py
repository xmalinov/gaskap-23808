from django.core.files import File
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse

from rest_framework import status

from classes.models import ClassVideo, ClassVideoComment
from classes.tests.factories import ClassFactory, ClassVideoFactory
from home.api.v1.tests.test_viewsets import AuthenticatedAPITestCase
from users.tests.factories import SchoolFactory, StudentFactory


class ClassVideoViewSetTestCase(AuthenticatedAPITestCase):
    def setUp(self):
        super().setUp()

        self.class_record = ClassFactory()

        self.filename = "test_file"
        self.file = File(open("static/test_file.json", "rb"))
        self.uploaded_file = SimpleUploadedFile(
            self.filename, self.file.read(), content_type="multipart/form-data"
        )

        self.school = SchoolFactory(student_code="Sj8bl", teacher_code="TeF61")
        StudentFactory(school=self.school, user=self.user)

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
                kwargs={"parent_lookup_uploaded_class": self.class_record.id + 1},
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
            "author": self.user.id,
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
        self.assertEqual(class_video.author.id, data.get("author"))


class ClassVideoCommentViewSetTestCase(AuthenticatedAPITestCase):
    def setUp(self):
        super().setUp()

        self.video = ClassVideoFactory()

        self.school = SchoolFactory(student_code="Sj8bl", teacher_code="TeF61")
        StudentFactory(school=self.school, user=self.user)

    def test_create_class_video_comment_with_invalid_class_id(self):
        data = {
            "content": "Test content",
            "author": self.user.id,
        }

        response = self.client.post(
            reverse(
                "classes-v1:class-video-comments-list",
                kwargs={
                    "parent_lookup_video__uploaded_class": self.video.uploaded_class.id
                    + 1,
                    "parent_lookup_video": self.video.id,
                },
            ),
            data=data,
        )

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_class_video_comment_with_invalid_video_id(self):
        data = {
            "content": "Test content",
            "author": self.user.id,
        }

        response = self.client.post(
            reverse(
                "classes-v1:class-video-comments-list",
                kwargs={
                    "parent_lookup_video__uploaded_class": self.video.uploaded_class.id,
                    "parent_lookup_video": self.video.id + 1,
                },
            ),
            data=data,
        )

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_class_video_comment(self):
        data = {
            "content": "Test content",
            "video": self.video.id,
            "author": self.user.id,
        }

        response = self.client.post(
            reverse(
                "classes-v1:class-video-comments-list",
                kwargs={
                    "parent_lookup_video__uploaded_class": self.video.uploaded_class.id,
                    "parent_lookup_video": self.video.id,
                },
            ),
            data=data,
        )

        video_comment = ClassVideoComment.objects.last()

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(video_comment.video.id, data.get("video"))
        self.assertEqual(video_comment.author.id, data.get("author"))
