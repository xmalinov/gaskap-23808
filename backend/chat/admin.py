from django.contrib import admin

from .models import Message, Thread


@admin.register(Thread)
class ThreadAdmin(admin.ModelAdmin):
    fields = ("participants",)
    list_display = (
        "id",
        "get_participants",
    )

    search_fields = ("id",)

    def get_participants(self, obj):
        return "\n".join([p.email for p in obj.participants.all()])


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("id", "contact", "content")

    search_fields = ("id", "contact__name", "content")
