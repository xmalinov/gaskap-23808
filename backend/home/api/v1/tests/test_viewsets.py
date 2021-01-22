import factory

from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase, APIClient

from users.tests.factories import UserFactory


class AuthenticatedAPITestCase(APITestCase):
    def setUp(self):
        self.user = UserFactory()
        self.user_pass = factory.Faker("password")
        self.user.set_password(self.user_pass)
        self.user.save()

        self.token = Token.objects.create(user=self.user)

        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token.key}")
