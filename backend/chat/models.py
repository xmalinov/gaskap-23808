from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django_extensions.db.models import TimeStampedModel


class Contact(TimeStampedModel):
    user = models.ForeignKey(
        "users.User",
        verbose_name=_("User"),
        on_delete=models.CASCADE,
        related_name="contacts",
    )
    contacts = models.ManyToManyField("self", blank=True, verbose_name=_("Contacts"))

    class Meta:
        verbose_name = _("Contact")
        verbose_name_plural = _("Contacts")

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse("Contact_detail", kwargs={"pk": self.pk})


class Message(TimeStampedModel):
    contact = models.ForeignKey(
        "chat.Contact",
        verbose_name=_("Contact"),
        related_name="messages",
        on_delete=models.CASCADE,
    )
    content = models.TextField(_("Content"))

    class Meta:
        verbose_name = _("Message")
        verbose_name_plural = _("Messages")

    def __str__(self):
        return self.contact.user.username

    def get_absolute_url(self):
        return reverse("Message_detail", kwargs={"pk": self.pk})


class Chat(models.Model):
    participants = models.ManyToManyField(
        "chat.Contact", related_name="chats", verbose_name=_("Participants")
    )
    messages = models.ManyToManyField(
        "chat.Message", blank=True, verbose_name=_("Messages")
    )

    class Meta:
        verbose_name = _("Chat")
        verbose_name_plural = _("Chats")

    def __str__(self):
        return "{}".format(self.pk)

    def get_absolute_url(self):
        return reverse("Chat_detail", kwargs={"pk": self.pk})
