import factory
from factory import post_generation
from faker import Factory

from users.tests.factories import UserFactory
from news.models import News, NewsComment

faker = Factory.create()


class NewsFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = News

    author = factory.SubFactory(UserFactory)
    headline = faker.text()
    description = faker.text()


class NewsCommentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = NewsComment

    author = factory.SubFactory(UserFactory)
    news = factory.SubFactory(NewsFactory)
    comment = faker.text()
