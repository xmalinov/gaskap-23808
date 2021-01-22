from django.db import models
from django_extensions.db.models import TimeStampedModel
from django.utils.translation import ugettext_lazy as _

from home.models import OPTIONAL
from home.utils import get_upload_path


class Class(TimeStampedModel):
    name = models.CharField(_("Name"), max_length=50)
    description = models.CharField(_("Description"), max_length=100, **OPTIONAL)
    start_time = models.TimeField(_("Start Time"))
    end_time = models.TimeField(_("End Time"))
    students = models.ManyToManyField(
        "users.Student", related_name="classes", blank=True
    )
    teacher = models.ForeignKey(
        "users.Teacher", related_name="teacher", on_delete=models.PROTECT
    )
    days = models.ManyToManyField("home.WeekDay", related_name="classes")

    class Meta:
        verbose_name = _("Class")
        verbose_name_plural = _("Classes")

    def __str__(self):
        return self.name


class ClassVideo(TimeStampedModel):
    name = models.CharField(_("Name"), max_length=50)
    description = models.TextField(_("Description"), **OPTIONAL)
    video = models.FileField(_("Video"), upload_to=get_upload_path)
    uploaded_class = models.ForeignKey(
        "classes.Class", related_name="videos", on_delete=models.PROTECT
    )
    author = models.ForeignKey(
        "users.User",
        related_name="class_video",
        on_delete=models.PROTECT,
    )

    class Meta:
        verbose_name = _("Class Video")
        verbose_name_plural = _("Class Videos")

    def __str__(self):
        return self.name


class ClassVideoComment(TimeStampedModel):
    content = models.TextField(_("Comment"))
    video = models.ForeignKey(
        "classes.ClassVideo",
        related_name="comments",
        on_delete=models.PROTECT,
    )
    author = models.ForeignKey(
        "users.User",
        related_name="class_video_comments",
        on_delete=models.PROTECT,
    )

    class Meta:
        verbose_name = _("Class Video Comment")
        verbose_name_plural = _("Class Video Comments")

    def __str__(self):
        return self.author.name or self.author.email
