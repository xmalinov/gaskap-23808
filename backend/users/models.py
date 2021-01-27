from django.contrib.auth.models import AbstractUser, UserManager as DjangoUserManager
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.crypto import get_random_string
from django.utils.translation import ugettext_lazy as _
from django_extensions.db.models import TimeStampedModel


from home.models import OPTIONAL
from home.utils import get_upload_path


class UserManager(DjangoUserManager):
    def active(self):
        return self.filter(is_active=True)


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

    name = models.CharField(_("Name of User"), **OPTIONAL, max_length=255)
    user_type = models.CharField(
        _("User Type"),
        max_length=50,
        choices=USER_TYPE_CHOICES,
        default=USER_TYPE_STUDENT,
    )

    objects = UserManager()

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})

    @property
    def profile(self):
        if self.user_type == self.USER_TYPE_SCHOOL:
            return self.school
        elif self.user_type == self.USER_TYPE_PARENT:
            return self.parent
        elif self.user_type == self.USER_TYPE_TEACHER:
            return self.teacher
        return self.student

    @property
    def is_student(self):
        return self.user_type == self.USER_TYPE_STUDENT

    @property
    def is_parent(self):
        return self.user_type == self.USER_TYPE_PARENT

    @property
    def is_teacher(self):
        return self.user_type == self.USER_TYPE_TEACHER

    @property
    def is_school(self):
        return self.user_type == self.USER_TYPE_SCHOOL

    def __str__(self):
        return self.name or self.email


class Profile(TimeStampedModel):
    phone_number = models.CharField(_("Phone number"), max_length=17, **OPTIONAL)
    state = models.CharField(_("State"), max_length=50, **OPTIONAL)
    city = models.CharField(_("City"), max_length=50, **OPTIONAL)
    date_of_birth = models.DateField(_("Date of birth"), **OPTIONAL)
    profile_picture = models.ImageField(
        _("Profile picture"), upload_to=get_upload_path, **OPTIONAL
    )

    class Meta:
        abstract = True

    @property
    def age(self):
        today = timezone.now()
        age = (
            today.year
            - self.date_of_birth.year
            - (
                (today.month, today.day)
                < (self.date_of_birth.month, self.date_of_birth.day)
            )
        )

        return age


class Student(Profile):
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
    GRADE_SENIOR = "senior"

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
        related_name="student",
        on_delete=models.CASCADE,
    )
    student_id = models.CharField(
        _("Student ID"), unique=True, max_length=50, **OPTIONAL
    )
    grade = models.CharField(
        _("Grade"), max_length=50, choices=GRADE_CHOICES, **OPTIONAL
    )
    school = models.ForeignKey(
        "users.School",
        verbose_name=_("School"),
        related_name="student",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.user.name or self.user.email


class Parent(Profile):
    user = models.OneToOneField(
        "users.User",
        verbose_name=_("User"),
        related_name="parent",
        on_delete=models.CASCADE,
    )
    students = models.ManyToManyField(
        "users.Student",
        related_name="parents",
    )

    def __str__(self):
        return self.user.name or self.user.email


class Teacher(Profile):
    user = models.OneToOneField(
        "users.User",
        verbose_name=_("User"),
        related_name="teacher",
        on_delete=models.CASCADE,
    )
    subject = models.CharField(_("Subject"), max_length=50, **OPTIONAL)
    school = models.ForeignKey(
        "users.School",
        verbose_name=_("School"),
        related_name="teacher",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.user.name or self.user.email


class School(Profile):
    user = models.OneToOneField(
        "users.User",
        verbose_name=_("User"),
        related_name="school",
        on_delete=models.CASCADE,
    )
    number = models.CharField(max_length=50, **OPTIONAL)
    about = models.TextField(_("About"), **OPTIONAL)
    student_code = models.CharField(
        _("Student Code"), max_length=50, unique=True, **OPTIONAL
    )
    teacher_code = models.CharField(
        _("Teacher Code"), max_length=50, unique=True, **OPTIONAL
    )
    color = models.CharField(_("Color"), max_length=100, **OPTIONAL)

    def __str__(self):
        return self.user.name or self.user.email
