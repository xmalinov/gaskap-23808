from datetime import date

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django_extensions.db.models import TimeStampedModel

from home.utils import get_upload_path


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
    name = models.CharField(_("Name of User"), blank=True, null=True, max_length=255)

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})


class Profile(TimeStampedModel):
    USER_TYPE_STUDENT = "student"
    USER_TYPE_TEACHER = "teacher"
    USER_TYPE_PARENT = "parent"
    USER_TYPE_SCHOOL = "school"

    USER_TYPE_CHOICES = [
        (USER_TYPE_STUDENT, "Student"),
        (USER_TYPE_TEACHER, "Teacher"),
        (USER_TYPE_PARENT, "Parent"),
        (USER_TYPE_SCHOOL, "School"),
    ]

    GRADE_KINDERGARTEN = "kindergarten"
    GRADE_FIRST = "first"
    GRADE_SECOND = "second"
    GRADE_THIRD = "third"
    GRADE_FORTH = "fourth"
    GRADE_FIFTH = "fifth"
    GRADE_SIXTH = "sixth"
    GRADE_SEVENTH = "seventh"
    GRADE_EIGTH = "eight"
    GRADE_FRESHMAN = "freshman"
    GRADE_SOPHOMORE = "sophomore"
    GRADE_JUNIOR = "junior"
    GRADE_SENIOR = "Senior"

    GRADE_CHOICES = [
        (GRADE_KINDERGARTEN, "Kindergarten"),
        (GRADE_FIRST, "First"),
        (GRADE_SECOND, "Second"),
        (GRADE_THIRD, "Third"),
        (GRADE_FORTH, "Fourth"),
        (GRADE_FIFTH, "Fifth"),
        (GRADE_SIXTH, "Sixth"),
        (GRADE_SEVENTH, "Seventh"),
        (GRADE_EIGTH, "Eigth"),
        (GRADE_FRESHMAN, "Freshman"),
        (GRADE_SOPHOMORE, "Sophomore"),
        (GRADE_JUNIOR, "Junior"),
        (GRADE_SENIOR, "Senior"),
    ]

    user = models.OneToOneField(
        "users.User",
        verbose_name=_("User"),
        related_name="profile",
        on_delete=models.CASCADE,
    )

    user_type = models.CharField(
        _("User Type"), max_length=50, choices=USER_TYPE_CHOICES
    )

    phone_number = models.CharField(_("Phone number"), max_length=17, blank=True)
    school = models.ForeignKey(
        "schools.School", related_name="profile", on_delete=models.SET_NULL, null=True
    )
    state = models.CharField(_("State"), max_length=50, null=True, blank=True)
    city = models.CharField(_("City"), max_length=50, null=True, blank=True)
    student_id = models.CharField(_("Student ID"), max_length=50, blank=True, null=True)
    grade = models.CharField(
        _("Grade"), max_length=50, choices=GRADE_CHOICES, blank=True, null=True
    )
    parent_guardian_name = models.CharField(_("Parent/Guardian Name"), max_length=100)
    date_of_birth = models.DateField(_("Date of birth"), null=True, blank=True)
    profile_pic = models.ImageField(
        _("Profile pic"), upload_to=get_upload_path, blank=True, null=True
    )

    def __str__(self):
        return self.user.name

    @property
    def age(self):
        today = date.today()
        age = (
            today.year
            - self.date_of_birth.year
            - (
                (today.month, today.day)
                < (self.date_of_birth.month, self.date_of_birth.day)
            )
        )

        return age
