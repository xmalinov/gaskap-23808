from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator
from django.http import HttpRequest
from django.utils.translation import ugettext_lazy as _

from allauth.account import app_settings as allauth_settings
from allauth.account.forms import ResetPasswordForm
from allauth.utils import email_address_exists, generate_unique_username
from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email
from rest_framework import serializers
from rest_auth.models import TokenModel
from rest_auth.serializers import PasswordResetSerializer
from rest_framework.validators import UniqueValidator

from home.models import CustomText, HomePage
from users.models import Profile
from schools.models import School

User = get_user_model()


class SignupSerializer(serializers.ModelSerializer):
    phone_number = serializers.CharField(label=_("Phone number"), write_only=True)
    user_type = serializers.CharField(label=_("User type"), write_only=True)
    school = serializers.IntegerField(
        label=_("School"),
        write_only=True,
        required=True,
    )
    parent_guardian_name = serializers.CharField(
        label=_("Parent/Guardian name"), write_only=True, required=True
    )

    class Meta:
        model = User
        fields = (
            "id",
            "name",
            "email",
            "password",
            "school",
            "user_type",
            "phone_number",
            "parent_guardian_name",
        )

        extra_kwargs = {
            "password": {"write_only": True, "style": {"input_type": "password"}},
            "email": {
                "required": True,
                "allow_blank": False,
            },
        }

    def _get_request(self):
        request = self.context.get("request")
        if (
            request
            and not isinstance(request, HttpRequest)
            and hasattr(request, "_request")
        ):
            request = request._request
        return request

    def validate_email(self, email):
        email = get_adapter().clean_email(email)
        if allauth_settings.UNIQUE_EMAIL:
            if email and email_address_exists(email):
                raise serializers.ValidationError(
                    _("A user is already registered with this e-mail address.")
                )
        return email

    def validate_user_type(self, user_type):
        if user_type not in [
            Profile.USER_TYPE_STUDENT,
            Profile.USER_TYPE_TEACHER,
            Profile.USER_TYPE_PARENT,
            Profile.USER_TYPE_SCHOOL,
        ]:
            raise serializers.ValidationError("Invalid user type.")

        return user_type

    def validate_phone_number(self, phone_number):
        phone_regex = RegexValidator(
            regex=r"^\+?1?\d{9,15}$",
            message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.",
        )
        phone_regex(phone_number)
        return phone_number

    def validate_school(self, school):
        school = School.objects.filter(id=school)
        if not school.exists():
            raise serializers.ValidationError("School does not exist.")
        return school.first()

    def create(self, validated_data):
        user = User(
            email=validated_data.get("email"),
            name=validated_data.get("name"),
            username=generate_unique_username(
                [validated_data.get("name"), validated_data.get("email"), "user"]
            ),
        )
        user.set_password(validated_data.get("password"))
        user.save()

        Profile.objects.create(
            user=user,
            user_type=validated_data.get("user_type"),
            phone_number=validated_data.get("phone_number"),
            school=validated_data.get("school"),
            parent_guardian_name=validated_data.get("parent_guardian_name"),
        )

        request = self._get_request()
        setup_user_email(request, user, [])
        return user

    def save(self, request=None):
        """rest_auth passes request so we must override to accept it"""
        return super().save()


class CustomTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomText
        fields = "__all__"


class HomePageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomePage
        fields = "__all__"


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = [
            "id",
            "user",
            "user_type",
            "phone_number",
            "school",
            "state",
            "city",
            "student_id",
            "school_id",
            "grade",
            "parent_guardian_name",
            "date_of_birth",
            "profile_pic",
        ]
        read_only_fields = ["id", "user"]


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = ["id", "email", "name", "profile", "is_active"]

    def update(self, instance, validated_data):
        profile = (
            validated_data.pop("profile") if validated_data.get("profile") else None
        )

        instance = super().update(instance, validated_data)

        if profile:
            Profile.objects.filter(user=instance).update(**profile)

        return instance


class PasswordSerializer(PasswordResetSerializer):
    """Custom serializer for rest_auth to solve reset password error"""

    password_reset_form_class = ResetPasswordForm


class TokenSerializer(serializers.ModelSerializer):
    """
    Serializer for Token model.
    """

    user = UserSerializer(read_only=True)

    class Meta:
        model = TokenModel
        fields = ("key", "user")
