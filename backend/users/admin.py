from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model

from users.forms import UserChangeForm, UserCreationForm
from .models import Profile

User = get_user_model()


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):

    form = UserChangeForm
    add_form = UserCreationForm
    fieldsets = (("User", {"fields": ("name",)}),) + auth_admin.UserAdmin.fieldsets
    list_display = ["username", "name", "email", "is_superuser"]
    search_fields = ["name"]


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):

    list_display = [
        "user",
        "user_type",
        "phone_number",
        "school",
        "state",
        "city",
        "student_id",
        "grade",
        "date_of_birth",
        "profile_pic",
    ]

    search_field = ["user__name", "student_id"]
