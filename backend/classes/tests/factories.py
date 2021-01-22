import factory
from factory import Faker, post_generation

from classes.models import Class, ClassVideo, ClassVideoComment
from home.tests.factories import WeekDayFactory
from users.tests.factories import UserFactory, TeacherFactory


class ClassFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Class

    name = factory.Faker("name")
    description = "Factory description"
    start_time = "13:00"
    end_time = "14:00"
    teacher = factory.SubFactory(TeacherFactory)


class ClassVideoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ClassVideo

    name = factory.Faker("name")
    description = "Factory description"
    video = factory.django.FileField(filename="the_file.dat")
    uploaded_class = factory.SubFactory(ClassFactory)
    author = factory.SubFactory(UserFactory)


class ClassVideoCommentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ClassVideoComment

    content = "Factory content"
    video = factory.SubFactory(ClassVideoFactory)
    author = factory.SubFactory(UserFactory)
