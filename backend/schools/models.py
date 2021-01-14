from django.db import models


class School(models.Model):
    number = models.CharField(max_length=50)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
