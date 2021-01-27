from django.urls import path, include

from rest_framework.routers import DefaultRouter

from users.api.v1 import viewsets

router = DefaultRouter()
router.register("", viewsets.UsersListViewSet, basename="users")


urlpatterns = [
    path("", include(router.urls)),
    path("profile/me/", viewsets.ProfileAPIView.as_view(), name="profile_edit"),
    path(
        "auth/email-confirmation/send/",
        viewsets.EmailConfirmation.as_view(),
        name="send-email-confirmation",
    ),
]
