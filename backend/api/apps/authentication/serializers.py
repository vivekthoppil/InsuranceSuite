from django.contrib.auth import authenticate
from django.core import exceptions as django_exceptions
from rest_framework import exceptions as drf_exceptions
from rest_framework import serializers

from .services import create_user_token


class RegistrationSerializer(serializers.Serializer):

    username = serializers.CharField(max_length=255, allow_blank=False)
    email = serializers.EmailField(max_length=255, allow_blank=False)
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=255)
    username = serializers.CharField(max_length=255, read_only=True)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        email = data.get('email', None)
        password = data.get('password', None)

        if email is None:
            raise serializers.ValidationError(
                'An email address is required to log in.'
            )

        if password is None:
            raise serializers.ValidationError(
                'A password is required to log in.'
            )

        user = authenticate(username=email, password=password)

        if user is None:
            raise drf_exceptions.AuthenticationFailed(
                'A user with this email and password was not found.'
            )

        if not user.is_active:
            raise drf_exceptions.AuthenticationFailed(
                'This user has been deactivated.'
            )

        try:
            token = create_user_token(user.email, user.password)
        except django_exceptions.ValidationError as ve:
            raise drf_exceptions.AuthenticationFailed(ve.message)

        return {
            'email': user.email,
            'username': user.username,
            'token': token
        }


class UserSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=255)
    username = serializers.CharField(max_length=255, read_only=True)
    password = serializers.CharField(max_length=128, write_only=True)
