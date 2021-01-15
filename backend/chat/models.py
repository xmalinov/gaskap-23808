from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django_extensions.db.models import TimeStampedModel


class Message(TimeStampedModel):
    contact = models.ForeignKey(
        "users.User",
        verbose_name=_("Contact"),
        related_name="messages",
        on_delete=models.CASCADE,
    )
    content = models.TextField(_("Content"))

    class Meta:
        verbose_name = _("Message")
        verbose_name_plural = _("Messages")

    def __str__(self):
        return self.content


class Thread(TimeStampedModel):
    participants = models.ManyToManyField(
        "users.User", related_name="threads", verbose_name=_("Participants")
    )
    messages = models.ManyToManyField(
        "chat.Message",
        verbose_name=_("Messages"),
        related_name="threads",
        blank=True,
    )

    class Meta:
        verbose_name = _("Thread")
        verbose_name_plural = _("Threads")

    def __str__(self):
        return f"{self.pk}"

    @staticmethod
    def get_last_10_messages(chat_id):
        return Thread.objects.get(pk=chat_id).messages.all()[:10]
