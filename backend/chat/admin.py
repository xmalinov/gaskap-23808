from django.contrib import admin

from .models import Message, Thread


@admin.register(Thread)
class ThreadAdmin(admin.ModelAdmin):
    fields = (
        "id",
        "participants",
    )
    list_display = (
        "id",
        "get_participants",
    )

    search_display = ("id",)

    def get_participants(self, obj):
        return "\n".join([f"{p.id}" for p in obj.participants.all()])


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("id", "contact", "content")

    search_display = ("id",)
