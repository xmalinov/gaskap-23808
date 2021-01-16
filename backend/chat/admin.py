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

    def get_participants(self, obj):
        return "\n".join([p.username for p in obj.participants.all()])


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("id", "contact", "content")
