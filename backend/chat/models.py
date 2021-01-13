from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from utils.models import BaseModel


class Chat(BaseModel):
    author = models.ForeignKey(
        "users.User", verbose_name=_("Author"), on_delete=models.CASCADE)
    content = models.TextField(_("Content"))

    class Meta:
        verbose_name = _("Chat")
        verbose_name_plural = _("Chats")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Chat_detail", kwargs={"pk": self.pk})
