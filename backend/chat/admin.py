from django.contrib import admin

from .models import Message, Thread

admin.site.register(Thread)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("contact", "content")
