from django.urls import path, include

from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers

from chat.api.v1 import viewsets

router = DefaultRouter()
router.register("threads", viewsets.ThreadViewSet, basename="threads")

message_router = routers.NestedSimpleRouter(router, r"threads", lookup="thread")

message_router.register(
    r"messages", viewsets.MessageViewSet, basename="thread-messages"
)

urlpatterns = [
    path("", include(router.urls)),
    path("", include(message_router.urls)),
]
