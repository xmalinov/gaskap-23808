from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django_extensions.db.models import TimeStampedModel


class News(TimeStampedModel):
    author = models.ForeignKey(
        "users.User",
        verbose_name=_("Author"),
        related_name="news",
        on_delete=models.PROTECT,
    )
    headline = models.CharField(_("Headline"), max_length=250)
    school = models.ForeignKey(
        "users.School", related_name="news", on_delete=models.PROTECT
    )
    description = models.TextField(_("Description"))

    class Meta:
        verbose_name = _("News")
        verbose_name_plural = _("News")
        ordering = ["-created"]

    def __str__(self):
        return self.headline


class NewsComment(TimeStampedModel):

    author = models.ForeignKey(
        "users.User",
        verbose_name=_("Author"),
        related_name="news_comment",
        on_delete=models.PROTECT,
    )

    news = models.ForeignKey(
        "news.News",
        verbose_name=_("news"),
        related_name="news_comments",
        on_delete=models.CASCADE,
    )

    comment = models.TextField(_("Comment"))

    class Meta:
        verbose_name = _("NewsComment")
        verbose_name_plural = _("NewsComments")
        ordering = ["-created"]

    def __str__(self):
        return self.comment
