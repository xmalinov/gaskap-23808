from django.contrib.auth import get_user_model
from django.http import HttpRequest
from django.utils.translation import ugettext_lazy as _
from allauth.account import app_settings as allauth_settings
from allauth.account.forms import ResetPasswordForm
from allauth.utils import email_address_exists, generate_unique_username
from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email
from rest_framework import serializers
from rest_auth.serializers import PasswordResetSerializer
from rest_framework.validators import UniqueValidator

from home.models import CustomText, HomePage
from users.models import Profile, UserType

User = get_user_model()


class SignupSerializer(serializers.ModelSerializer):
    name = serializers.CharField(label=_("Full name"))
    phone_number = serializers.CharField(
        label=_("Phone number"), write_only=True)
    user_type = serializers.IntegerField(label=_("User type"), write_only=True)
    school = serializers.CharField(
        label=_("School"), write_only=True, required=False, allow_null=True)

    class Meta:
        model = User
        fields = ('id', 'name', 'email', 'password',  'school',
                  'user_type', 'phone_number', 'name')

        phone_number = serializers.CharField(
            max_length=15,
            validators=[
                UniqueValidator(
                    queryset=Profile.objects.all(),
                    message="A user is already registered with this phone number.",
                )
            ]
        )

        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {
                    'input_type': 'password'
                }
            },
            'email': {
                'required': True,
                'allow_blank': False,
            }
        }

    def _get_request(self):
        request = self.context.get('request')
        if request and not isinstance(request, HttpRequest) and hasattr(request, '_request'):
            request = request._request
        return request

    def validate_email(self, email):
        email = get_adapter().clean_email(email)
        if allauth_settings.UNIQUE_EMAIL:
            if email and email_address_exists(email):
                raise serializers.ValidationError(
                    _("A user is already registered with this e-mail address."))
        return email

    def validate_user_type(self, user_type):
        try:
            user_type_insance = UserType.objects.get(id=user_type)
        except UserType.DoesNotExist:
            raise serializers.ValidationError(
                _("The provided user type id does not exist")
            )
        return user_type_insance

    def create(self, validated_data):
        user_type = validated_data.pop("user_type")
        phone_number = validated_data.pop("phone_number")
        school = validated_data.pop(
            "school") if "school" in validated_data else None
        user = User(
            email=validated_data.get('email'),
            name=validated_data.get('name'),
            username=generate_unique_username([
                validated_data.get('name'),
                validated_data.get('email'),
                'user'
            ])
        )
        user.set_password(validated_data.get('password'))
        user.save()

        profile = Profile()
        profile.user = user
        profile.user_type = user_type
        profile.phone_number = phone_number
        profile.school = school
        profile.save()
        request = self._get_request()
        setup_user_email(request, user, [])
        return user

    def save(self, request=None):
        """rest_auth passes request so we must override to accept it"""
        return super().save()


class CustomTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomText
        fields = '__all__'


class HomePageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomePage
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'name']


class PasswordSerializer(PasswordResetSerializer):
    """Custom serializer for rest_auth to solve reset password error"""
    password_reset_form_class = ResetPasswordForm


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
