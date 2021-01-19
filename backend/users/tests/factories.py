import factory
from factory import Faker, post_generation
from typing import Any, Sequence

from django.contrib.auth import get_user_model
from django.utils.crypto import get_random_string

from allauth.account.models import EmailAddress

from users import models


class UserFactory(factory.django.DjangoModelFactory):

    username = Faker("user_name")
    email = Faker("email")
    name = Faker("name")

    @post_generation
    def password(self, create: bool, extracted: Sequence[Any], **kwargs):
        password = Faker(
            "password",
            length=42,
            special_chars=True,
            digits=True,
            upper_case=True,
            lower_case=True,
        )
        self.set_password(password)

    class Meta:
        model = get_user_model()
        django_get_or_create = ["username"]


class SchoolFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.School

    user = factory.SubFactory(UserFactory)
    number = get_random_string(length=8)
    about = "Factory About"
    student_code = get_random_string(length=8)
    teacher_code = get_random_string(length=8)
    color = "Blue"


class StudentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Student

    user = factory.SubFactory(UserFactory)
    student_id = get_random_string(length=8)
    grade = "sophomore"
    school = factory.SubFactory(SchoolFactory)


class ParentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Parent

    user = factory.SubFactory(UserFactory)


class TeacherFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Teacher

    user = factory.SubFactory(UserFactory)
    school = factory.SubFactory(SchoolFactory)
    subject = "math"


class EmailAddressFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = EmailAddress

    user = factory.SubFactory(UserFactory)
