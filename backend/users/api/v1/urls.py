from django.urls import path, include

from users.api.v1 import viewsets


urlpatterns = [
    path("profile/me/", viewsets.ProfileAPIView.as_view(), name="profile_edit"),
]
