from django.urls import path, include

from rest_framework.routers import DefaultRouter

from chat.api.v1 import viewsets

router = DefaultRouter()
router.register("", viewsets.ChatViewSet, basename="chat")

urlpatterns = [
    path("", include(router.urls)),
]
