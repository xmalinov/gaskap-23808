from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model

from users.forms import UserChangeForm, UserCreationForm

from .models import Student, Parent, Teacher, School

User = get_user_model()


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):

    form = UserChangeForm
    add_form = UserCreationForm
    fieldsets = (
        (
            "User",
            {
                "fields": (
                    "name",
                    "user_type",
                )
            },
        ),
    ) + auth_admin.UserAdmin.fieldsets
    list_display = ["username", "user_type", "name", "email", "is_superuser"]
    search_fields = ["name"]


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "student_id",
        "grade",
        "school",
    ]
    search_field = ["user__name", "student_id"]
    raw_id_fields = ["user", "school"]


@admin.register(Parent)
class ParentAdmin(admin.ModelAdmin):
    list_display = [
        "user",
    ]
    search_field = ["user__name"]
    raw_id_fields = ["user", "students"]


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ["user", "subject"]
    search_field = ["user__name", "subject"]
    raw_id_fields = ["user", "school"]


@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "student_code",
        "teacher_code",
    ]
    search_field = ["user__name", "student_code", "teacher_code"]
    raw_id_fields = ["user"]
