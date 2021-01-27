from django.db import models
from django.utils.translation import ugettext_lazy as _


OPTIONAL = {
    "blank": True,
    "null": True,
}


class WeekDay(models.Model):
    DAY_MONDAY = "monday"
    DAY_TUESDAY = "tuesday"
    DAY_WEDNESDAY = "wednesday"
    DAY_THURSDAY = "thursday"
    DAY_FRIDAY = "friday"
    DAY_SATURDAY = "saturday"
    DAY_SUNDAY = "sunday"

    DAY_CHOICES = [
        (DAY_MONDAY, "Monday"),
        (DAY_TUESDAY, "Tuesday"),
        (DAY_WEDNESDAY, "Wednesday"),
        (DAY_THURSDAY, "Thursday"),
        (DAY_FRIDAY, "Friday"),
        (DAY_SATURDAY, "Saturday"),
        (DAY_SUNDAY, "Sunday"),
    ]

    name = models.CharField(_("Day"), max_length=20, choices=DAY_CHOICES, unique=True)

    class Meta:
        verbose_name = _("Week Day")
        verbose_name_plural = _("Week Days")

    def __str__(self):
        return self.get_name_display()
