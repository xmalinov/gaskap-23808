from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from utils.models import BaseModel


class User(AbstractUser):
    # WARNING!
    """
    Some officially supported features of Crowdbotics Dashboard depend on the initial
    state of this User model (Such as the creation of superusers using the CLI
    or password reset in the dashboard). Changing, extending, or modifying this model
    may lead to unexpected bugs and or behaviors in the automated flows provided
    by Crowdbotics. Change it at your own risk.
    """

    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = models.CharField(_("Name of User"), blank=True,
                            null=True, max_length=255)

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})


class UserType(BaseModel):
    STUDENT = 1
    TEACHER = 2
    PARENT = 3
    SCHOOL = 4

    TYPE_CHOICES = [
        (STUDENT, "student"),
        (TEACHER, "teacher"),
        (PARENT, "parent"),
        (SCHOOL, "school"),
    ]

    id = models.PositiveSmallIntegerField(
        choices=TYPE_CHOICES, primary_key=True)

    class Meta:
        verbose_name = _("StudentType")
        verbose_name_plural = _("UserTypes")

    def __str__(self):
        return self.get_id_display()

    def get_absolute_url(self):
        return reverse("UserType_detail", kwargs={"pk": self.pk})


class Grade(BaseModel):
    KINDERGARTEN = 1
    FIRST = 2
    SECOND = 3
    THIRD = 4
    FORTH = 5
    FIFTH = 6
    SIXTH = 7
    SEVENTH = 8
    EIGTH = 9
    FRESHMAN = 10
    SOFTMORE = 11
    JUNIOR = 12
    SENIOR = 13

    GRADE_CHOICES = [
        (KINDERGARTEN, "kindergarten"),
        (FIRST, "first"),
        (SECOND, "second"),
        (THIRD, "third"),
        (FORTH, "forth"),
        (FIFTH, "fifth"),
        (SIXTH, "sixth"),
        (SEVENTH, "seventh"),
        (EIGTH, "eigth"),
        (FRESHMAN, "freshman"),
        (SOFTMORE, "softmore"),
        (JUNIOR, "junior"),
        (SENIOR, "senior")
    ]

    id = models.PositiveSmallIntegerField(
        choices=GRADE_CHOICES, primary_key=True)

    class Meta:
        verbose_name = _("Grade")
        verbose_name_plural = _("Grades")

    def __str__(self):
        return self.get_id_display()

    def get_absolute_url(self):
        return reverse("Grade_detail", kwargs={"pk": self.pk})


class Profile(BaseModel):
    user = models.OneToOneField("users.User", verbose_name=_(
        "User"), related_name="user_profile", on_delete=models.CASCADE)

    user_type = models.ForeignKey(
        "users.UserType", verbose_name=_("User Type"), on_delete=models.CASCADE, related_name="profile", default=1)
    phone_number = models.CharField(_("Phone number"), max_length=50)
    school = models.CharField(
        _("School"), max_length=50, null=True, blank=True)
    state = models.CharField(_("State"), max_length=50, null=True, blank=True)
    city = models.CharField(_("City"), max_length=50, null=True, blank=True)
    student_id = models.CharField(
        _("Student ID"), max_length=50, blank=True, null=True)
    grade = models.ForeignKey("users.Grade", verbose_name=_(
        "Grade"), on_delete=models.CASCADE, related_name="profile", null=True, blank=True)
    dob = models.DateField(_("Date of birth"), null=True, blank=True)
    profile_pic = models.ImageField(
        _("Profile pic"), upload_to=None, blank=True, null=True)
