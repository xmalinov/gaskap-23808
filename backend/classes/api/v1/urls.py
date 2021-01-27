from django.urls import path, include

from rest_framework_extensions.routers import ExtendedDefaultRouter

from classes.api.v1 import viewsets


router = ExtendedDefaultRouter()

class_router = router.register(r"", viewsets.ClassViewSet, basename="classes")

students_router = class_router.register(
    r"students",
    viewsets.ClassStudentViewSet,
    basename="class-students",
    parents_query_lookups=["student__classes"],
)
video_router = class_router.register(
    r"videos",
    viewsets.ClassVideoViewSet,
    basename="class-videos",
    parents_query_lookups=["uploaded_class"],
)

comment_router = video_router.register(
    r"comments",
    viewsets.ClassVideoCommentViewSet,
    basename="class-video-comments",
    parents_query_lookups=["video__uploaded_class", "video"],
)


urlpatterns = [
    path("", include(router.urls)),
]
