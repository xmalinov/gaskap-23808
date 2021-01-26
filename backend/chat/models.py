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
    thread = models.ForeignKey(
        "chat.Thread",
        related_name="messages",
        verbose_name=_("Thread"),
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = _("Message")
        verbose_name_plural = _("Messages")
        ordering = ["-id"]

    def __str__(self):
        return self.content


class Thread(TimeStampedModel):
    participants = models.ManyToManyField(
        "users.User", related_name="threads", verbose_name=_("Participants")
    )

    class Meta:
        verbose_name = _("Thread")
        verbose_name_plural = _("Threads")
        ordering = ["-id"]

    def __str__(self):
        return f"{self.pk}"
