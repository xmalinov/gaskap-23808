from unittest.mock import MagicMock

from django.test import TestCase
from django.test.client import RequestFactory

from classes.api.v1.permissions import (
    HasClassPermission,
    HasClassVideoCommentPermission,
    HasClassVideoPermission,
)
from users.tests.factories import UserFactory


class PermissionRequestViewTestCase(TestCase):
    def setUp(self):
        self.student = UserFactory(user_type="student")
        self.parent = UserFactory(user_type="parent")
        self.teacher = UserFactory(user_type="teacher")
        self.school = UserFactory(user_type="school")

        self.mock = MagicMock()

        self.mock_student_request = MagicMock(user=self.student)
        self.mock_parent_request = MagicMock(user=self.parent)
        self.mock_teacher_request = MagicMock(user=self.teacher)
        self.mock_school_request = MagicMock(user=self.school)

        self.mock_view_create = MagicMock(action="create")
        self.mock_view_update = MagicMock(action="update")
        self.mock_view_partial_update = MagicMock(action="partial_update")
        self.mock_view_destroy = MagicMock(action="destroy")


class TestHasClassPermissionTestCase(PermissionRequestViewTestCase):
    def test_create_class_as_student(self):
        self.assertFalse(
            HasClassPermission.has_permission(
                self=self.mock,
                request=self.mock_student_request,
                view=self.mock_view_create,
            )
        )

    def test_create_class_as_parent(self):
        self.assertFalse(
            HasClassPermission.has_permission(
                self=self.mock,
                request=self.mock_parent_request,
                view=self.mock_view_create,
            )
        )

    def test_create_class_as_teacher(self):
        self.assertTrue(
            HasClassPermission.has_permission(
                self=self.mock,
                request=self.mock_teacher_request,
                view=self.mock_view_create,
            )
        )

    def test_create_class_as_school(self):
        self.assertTrue(
            HasClassPermission.has_permission(
                self=self.mock,
                request=self.mock_school_request,
                view=self.mock_view_create,
            )
        )

    def test_partial_update_class_as_student(self):
        self.assertFalse(
            HasClassPermission.has_permission(
                self=self.mock,
                request=self.mock_student_request,
                view=self.mock_view_partial_update,
            )
        )

    def test_partial_update_class_as_parent(self):
        self.assertFalse(
            HasClassPermission.has_permission(
                self=self.mock,
                request=self.mock_parent_request,
                view=self.mock_view_partial_update,
            )
        )

    def test_partial_update_class_as_teacher(self):
        self.assertTrue(
            HasClassPermission.has_permission(
                self=self.mock,
                request=self.mock_teacher_request,
                view=self.mock_view_partial_update,
            )
        )

    def test_partial_update_class_as_school(self):
        self.assertTrue(
            HasClassPermission.has_permission(
                self=self.mock,
                request=self.mock_school_request,
                view=self.mock_view_partial_update,
            )
        )

    def test_update_class_as_student(self):
        self.assertFalse(
            HasClassPermission.has_permission(
                self=self.mock,
                request=self.mock_student_request,
                view=self.mock_view_update,
            )
        )

    def test_update_class_as_parent(self):
        self.assertFalse(
            HasClassPermission.has_permission(
                self=self.mock,
                request=self.mock_parent_request,
                view=self.mock_view_update,
            )
        )

    def test_update_class_as_teacher(self):
        self.assertTrue(
            HasClassPermission.has_permission(
                self=self.mock,
                request=self.mock_teacher_request,
                view=self.mock_view_update,
            )
        )

    def test_update_class_as_school(self):
        self.assertTrue(
            HasClassPermission.has_permission(
                self=self.mock,
                request=self.mock_school_request,
                view=self.mock_view_update,
            )
        )

    def test_delete_class_as_student(self):
        self.assertFalse(
            HasClassPermission.has_permission(
                self=self.mock,
                request=self.mock_student_request,
                view=self.mock_view_destroy,
            )
        )

    def test_delete_class_as_parent(self):
        self.assertFalse(
            HasClassPermission.has_permission(
                self=self.mock,
                request=self.mock_parent_request,
                view=self.mock_view_destroy,
            )
        )

    def test_delete_class_as_teacher(self):
        self.assertFalse(
            HasClassPermission.has_permission(
                self=self.mock,
                request=self.mock_teacher_request,
                view=self.mock_view_destroy,
            )
        )

    def test_delete_class_as_school(self):
        self.assertTrue(
            HasClassPermission.has_permission(
                self=self.mock,
                request=self.mock_school_request,
                view=self.mock_view_destroy,
            )
        )


class TestHasClassVideoPermissionTestCase(PermissionRequestViewTestCase):
    def test_create_class_video_as_student(self):
        self.assertFalse(
            HasClassVideoPermission.has_permission(
                self=self.mock,
                request=self.mock_student_request,
                view=self.mock_view_create,
            )
        )

    def test_create_class_video_as_parent(self):
        self.assertFalse(
            HasClassVideoPermission.has_permission(
                self=self.mock,
                request=self.mock_parent_request,
                view=self.mock_view_create,
            )
        )

    def test_create_class_video_as_teacher(self):
        self.assertTrue(
            HasClassVideoPermission.has_permission(
                self=self.mock,
                request=self.mock_teacher_request,
                view=self.mock_view_create,
            )
        )

    def test_create_class_video_as_school(self):
        self.assertTrue(
            HasClassVideoPermission.has_permission(
                self=self.mock,
                request=self.mock_school_request,
                view=self.mock_view_create,
            )
        )

    def test_partial_update_class_video_as_student(self):
        self.assertFalse(
            HasClassVideoPermission.has_permission(
                self=self.mock,
                request=self.mock_student_request,
                view=self.mock_view_partial_update,
            )
        )

    def test_partial_update_class_video_as_parent(self):
        self.assertFalse(
            HasClassVideoPermission.has_permission(
                self=self.mock,
                request=self.mock_parent_request,
                view=self.mock_view_partial_update,
            )
        )

    def test_partial_update_class_video_as_teacher(self):
        self.assertTrue(
            HasClassVideoPermission.has_permission(
                self=self.mock,
                request=self.mock_teacher_request,
                view=self.mock_view_partial_update,
            )
        )

    def test_partial_update_class_video_as_school(self):
        self.assertTrue(
            HasClassVideoPermission.has_permission(
                self=self.mock,
                request=self.mock_school_request,
                view=self.mock_view_partial_update,
            )
        )

    def test_update_class_video_as_student(self):
        self.assertFalse(
            HasClassVideoPermission.has_permission(
                self=self.mock,
                request=self.mock_student_request,
                view=self.mock_view_update,
            )
        )

    def test_update_class_video_as_parent(self):
        self.assertFalse(
            HasClassVideoPermission.has_permission(
                self=self.mock,
                request=self.mock_parent_request,
                view=self.mock_view_update,
            )
        )

    def test_update_class_video_as_teacher(self):
        self.assertTrue(
            HasClassVideoPermission.has_permission(
                self=self.mock,
                request=self.mock_teacher_request,
                view=self.mock_view_update,
            )
        )

    def test_update_class_video_as_school(self):
        self.assertTrue(
            HasClassVideoPermission.has_permission(
                self=self.mock,
                request=self.mock_school_request,
                view=self.mock_view_update,
            )
        )

    def test_delete_class_video_as_student(self):
        self.assertFalse(
            HasClassVideoPermission.has_permission(
                self=self.mock,
                request=self.mock_student_request,
                view=self.mock_view_destroy,
            )
        )

    def test_delete_class_video_as_parent(self):
        self.assertFalse(
            HasClassVideoPermission.has_permission(
                self=self.mock,
                request=self.mock_parent_request,
                view=self.mock_view_destroy,
            )
        )

    def test_delete_class_video_as_teacher(self):
        self.assertTrue(
            HasClassVideoPermission.has_permission(
                self=self.mock,
                request=self.mock_teacher_request,
                view=self.mock_view_destroy,
            )
        )

    def test_delete_class_video_as_school(self):
        self.assertTrue(
            HasClassVideoPermission.has_permission(
                self=self.mock,
                request=self.mock_school_request,
                view=self.mock_view_destroy,
            )
        )


class TestHasClassVideoCommentPermissionTestCase(PermissionRequestViewTestCase):
    def test_create_class_video_comment_as_student(self):
        self.assertFalse(
            HasClassVideoCommentPermission.has_permission(
                self=self.mock,
                request=self.mock_student_request,
                view=self.mock_view_create,
            )
        )

    def test_create_class_video_comment_as_parent(self):
        self.assertFalse(
            HasClassVideoCommentPermission.has_permission(
                self=self.mock,
                request=self.mock_parent_request,
                view=self.mock_view_create,
            )
        )

    def test_create_class_video_comment_as_school(self):
        self.assertFalse(
            HasClassVideoCommentPermission.has_permission(
                self=self.mock,
                request=self.mock_school_request,
                view=self.mock_view_create,
            )
        )

    def test_create_class_video_comment_as_teacher(self):
        self.assertTrue(
            HasClassVideoCommentPermission.has_permission(
                self=self.mock,
                request=self.mock_teacher_request,
                view=self.mock_view_create,
            )
        )

    def test_partial_update_class_video_comment_as_student(self):
        self.assertFalse(
            HasClassVideoCommentPermission.has_permission(
                self=self.mock,
                request=self.mock_student_request,
                view=self.mock_view_partial_update,
            )
        )

    def test_partial_update_class_video_comment_as_parent(self):
        self.assertFalse(
            HasClassVideoCommentPermission.has_permission(
                self=self.mock,
                request=self.mock_parent_request,
                view=self.mock_view_partial_update,
            )
        )

    def test_partial_update_class_video_comment_as_school(self):
        self.assertFalse(
            HasClassVideoCommentPermission.has_permission(
                self=self.mock,
                request=self.mock_school_request,
                view=self.mock_view_partial_update,
            )
        )

    def test_partial_update_class_video_comment_as_teacher(self):
        self.assertTrue(
            HasClassVideoCommentPermission.has_permission(
                self=self.mock,
                request=self.mock_teacher_request,
                view=self.mock_view_partial_update,
            )
        )

    def test_update_class_video_comment_as_student(self):
        self.assertFalse(
            HasClassVideoCommentPermission.has_permission(
                self=self.mock,
                request=self.mock_student_request,
                view=self.mock_view_update,
            )
        )

    def test_update_class_video_comment_as_parent(self):
        self.assertFalse(
            HasClassVideoCommentPermission.has_permission(
                self=self.mock,
                request=self.mock_parent_request,
                view=self.mock_view_update,
            )
        )

    def test_update_class_video_comment_as_school(self):
        self.assertFalse(
            HasClassVideoCommentPermission.has_permission(
                self=self.mock,
                request=self.mock_school_request,
                view=self.mock_view_update,
            )
        )

    def test_update_class_video_comment_as_teacher(self):
        self.assertTrue(
            HasClassVideoCommentPermission.has_permission(
                self=self.mock,
                request=self.mock_teacher_request,
                view=self.mock_view_update,
            )
        )

    def test_delete_class_video_comment_as_student(self):
        self.assertFalse(
            HasClassVideoCommentPermission.has_permission(
                self=self.mock,
                request=self.mock_student_request,
                view=self.mock_view_destroy,
            )
        )

    def test_delete_class_video_comment_as_parent(self):
        self.assertFalse(
            HasClassVideoCommentPermission.has_permission(
                self=self.mock,
                request=self.mock_parent_request,
                view=self.mock_view_destroy,
            )
        )

    def test_delete_class_video_comment_as_school(self):
        self.assertFalse(
            HasClassVideoCommentPermission.has_permission(
                self=self.mock,
                request=self.mock_school_request,
                view=self.mock_view_destroy,
            )
        )

    def test_delete_class_video_comment_as_teacher(self):
        self.assertTrue(
            HasClassVideoCommentPermission.has_permission(
                self=self.mock,
                request=self.mock_teacher_request,
                view=self.mock_view_destroy,
            )
        )
