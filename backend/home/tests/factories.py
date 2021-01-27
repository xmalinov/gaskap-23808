import factory

from home import models


class WeekDayFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.WeekDay

    name = "Monday"
