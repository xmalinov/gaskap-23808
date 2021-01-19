from allauth.account.models import EmailAddress
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.generics import GenericAPIView

from home.api.v1.serializers import EmailResetSerializer


class EmailConfirmation(GenericAPIView):
    """Resend email verification"""

    serializer_class = EmailResetSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        email_addresses = EmailAddress.objects.filter(email=request.data.get("email"))
        if not email_addresses.exists():
            return Response(
                {"message": "Email does not exist."}, status=status.HTTP_400_BAD_REQUEST
            )

        email_address = email_addresses.first()
        if email_address.verified:
            return Response(
                {"message": "Email already verified"},
                status=status.HTTP_200_OK,
            )

        email_address.send_confirmation(request=request, signup=False)
        return Response(
            {"message": "Email confirmation sent"}, status=status.HTTP_200_OK
        )
