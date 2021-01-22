from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator
from django.db import transaction
from django.http import HttpRequest
from django.utils.translation import ugettext_lazy as _

from allauth.account import app_settings as allauth_settings
from allauth.account.forms import ResetPasswordForm
from allauth.account.models import EmailAddress
from allauth.utils import email_address_exists, generate_unique_username
from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email
from rest_framework import serializers
from rest_auth.models import TokenModel
from rest_auth.serializers import PasswordResetSerializer
from rest_framework.validators import UniqueValidator

from users.models import Student, Parent, Teacher, School

User = get_user_model()


class SignupSerializer(serializers.ModelSerializer):
    phone_number = serializers.CharField(label=_("Phone number"), write_only=True)
    user_type = serializers.CharField(label=_("User type"), write_only=True)
    code = serializers.CharField(
        label=_("Code"),
        write_only=True,
        required=False,
    )

    class Meta:
        model = User
        fields = (
            "id",
            "name",
            "email",
            "password",
            "code",
            "user_type",
            "phone_number",
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
            User.USER_TYPE_STUDENT,
            User.USER_TYPE_TEACHER,
            User.USER_TYPE_PARENT,
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

    def validate_code(self, code):
        user_type = self.initial_data.get("user_type")

        if (
            user_type == User.USER_TYPE_STUDENT
            and not School.objects.filter(student_code=code).exists()
        ):
            raise serializers.ValidationError("Code is invalid.")
        elif (
            user_type == User.USER_TYPE_PARENT
            and not Student.objects.filter(student_id=code).exists()
        ):
            raise serializers.ValidationError("Student ID is invalid.")
        elif (
            user_type == User.USER_TYPE_TEACHER
            and not School.objects.filter(teacher_code=code).exists()
        ):
            raise serializers.ValidationError("Code is invalid.")

        return code

    def create(self, validated_data):
        user_type = validated_data.get("user_type")
        user = User(
            email=validated_data.get("email"),
            name=validated_data.get("name"),
            username=generate_unique_username(
                [validated_data.get("name"), validated_data.get("email"), "user"]
            ),
            user_type=user_type,
        )
        user.set_password(validated_data.get("password"))
        user.save()

        if user_type == User.USER_TYPE_STUDENT:
            school = School.objects.filter(
                student_code=validated_data.get("code")
            ).first()
            Student.objects.create(
                user=user,
                phone_number=validated_data.get("phone_number"),
                school=school,
            )

        elif user_type == User.USER_TYPE_PARENT:
            parent = Parent.objects.create(
                user=user,
                phone_number=validated_data.get("phone_number"),
            )
            student = Student.objects.filter(
                student_id=validated_data.get("code")
            ).first()
            parent.students.add(student)

        elif user_type == User.USER_TYPE_TEACHER:
            school = School.objects.filter(
                teacher_code=validated_data.get("code")
            ).first()
            Teacher.objects.create(
                user=user,
                phone_number=validated_data.get("phone_number"),
                school=school,
            )

        request = self._get_request()
        setup_user_email(request, user, [])
        return user

    def save(self, request=None):
        """rest_auth passes request so we must override to accept it"""
        return super().save()


class ProfileSerializer(serializers.ModelSerializer):
    def validate_phone_number(self, phone_number):
        phone_regex = RegexValidator(
            regex=r"^\+?1?\d{9,15}$",
            message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.",
        )
        phone_regex(phone_number)
        return phone_number


class SchoolSerializer(ProfileSerializer):
    class Meta:
        model = School
        fields = [
            "id",
            "user",
            "number",
            "phone_number",
            "state",
            "city",
            "profile_picture",
            "color",
        ]
        read_only_fields = ["user"]


class StudentSerializer(ProfileSerializer):
    school = SchoolSerializer(read_only=True)

    class Meta:
        model = Student
        fields = [
            "id",
            "user",
            "phone_number",
            "school",
            "state",
            "city",
            "student_id",
            "grade",
            "date_of_birth",
            "profile_picture",
        ]
        read_only_fields = ["user", "school"]


class ParentSerializer(ProfileSerializer):
    students = StudentSerializer(many=True, read_only=True)

    class Meta:
        model = Parent
        fields = [
            "id",
            "user",
            "phone_number",
            "state",
            "city",
            "date_of_birth",
            "profile_picture",
            "students",
        ]
        read_only_fields = ["user", "students"]


class TeacherSerializer(ProfileSerializer):
    school = SchoolSerializer(read_only=True)

    class Meta:
        model = Teacher
        fields = [
            "id",
            "user",
            "phone_number",
            "school",
            "state",
            "city",
            "date_of_birth",
            "profile_picture",
            "subject",
        ]
        read_only_fields = ["user", "school"]


class UserSerializer(serializers.ModelSerializer):
    profile = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ["id", "email", "name", "user_type", "profile", "is_active"]
        read_only_fields = ["user_type"]

    def get_profile(self, obj):
        if obj.user_type == User.USER_TYPE_SCHOOL:
            return SchoolSerializer(instance=obj.profile).data
        elif obj.user_type == User.USER_TYPE_PARENT:
            return ParentSerializer(instance=obj.profile).data
        elif obj.user_type == User.USER_TYPE_TEACHER:
            return TeacherSerializer(instance=obj.profile).data
        else:
            return StudentSerializer(instance=obj.profile).data

    @transaction.atomic
    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data)
        # Updates stored EmailAddress
        if validated_data.get("email"):
            EmailAddress.objects.filter(user=instance).update(
                email=validated_data.get("email")
            )

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


class EmailResetSerializer(serializers.Serializer):
    email = serializers.EmailField()
