from allauth.account.auth_backends import (
    AuthenticationBackend as AllAuthAuthenticationBackend,
)


class AuthenticationBackend(AllAuthAuthenticationBackend):
    def user_can_authenticate(self, user):
        return True
