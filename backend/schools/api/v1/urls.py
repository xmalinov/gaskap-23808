from django.urls import path, include

from rest_framework.routers import DefaultRouter

from schools.api.v1 import viewsets

router = DefaultRouter()
router.register("", viewsets.SchoolViewSet, basename="schools")

urlpatterns = [
    path("", include(router.urls)),
]
