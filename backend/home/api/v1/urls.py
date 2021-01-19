from django.urls import path, include

from home.api.v1 import viewsets

urlpatterns = [
    path(
        "auth/email-confirmation/send/",
        viewsets.EmailConfirmation.as_view(),
        name="send-email-confirmation",
    ),
]
