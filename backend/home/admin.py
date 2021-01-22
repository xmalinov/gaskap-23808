from django.contrib import admin

from home.models import WeekDay


@admin.register(WeekDay)
class WeekDayAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
    ]
    search_field = ["name"]
