import factory
from factory import post_generation
from faker import Factory

from users.tests.factories import UserFactory
from chat import models


faker = Factory.create()


class ThreadFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Thread

    @post_generation
    def participants(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for participant in extracted:
                self.participants.add(participant)


class MessageFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Message

    contact = factory.SubFactory(UserFactory)
    content = faker.text()
    thread = factory.SubFactory(ThreadFactory)
