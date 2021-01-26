import factory

from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase, APIClient

from users.tests.factories import UserFactory
from users.models import User


class AuthenticatedAPITestCase(APITestCase):
    def setUp(self):
        self.user = UserFactory()
        self.user_pass = factory.Faker("password")
        self.user.set_password(self.user_pass)
        self.user.save()

        self.school_user = UserFactory(user_type=User.USER_TYPE_SCHOOL)
        self.school_user_pass = factory.Faker("password")
        self.school_user.set_password(self.user_pass)
        self.school_user.save()

        self.token = Token.objects.create(user=self.user)
        self.school_token = Token.objects.create(user=self.school_user)

        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token.key}")

        self.school_client = APIClient()
        self.school_client.credentials(
            HTTP_AUTHORIZATION=f"Token {self.school_token.key}"
        )
