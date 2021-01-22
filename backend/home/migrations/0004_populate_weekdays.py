from django.db import migrations, models
import django.db.models.deletion

from home.models import WeekDay


def add_days(apps, schema_editor):
    WeekDayModel = apps.get_model("home", "WeekDay")

    for day in WeekDay.DAY_CHOICES:
        WeekDayModel.objects.create(name=day[0])


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0003_auto_20210122_1139"),
    ]

    operations = [migrations.RunPython(add_days, migrations.RunPython.noop)]
