from django.urls import path, include

from rest_framework.routers import DefaultRouter

from chat.api.v1 import viewsets

router = DefaultRouter()
router.register("thread", viewsets.ThreadViewSet, basename="thread")
router.register("message", viewsets.MessageViewSet, basename="message")

urlpatterns = [
    path("", include(router.urls)),
]
