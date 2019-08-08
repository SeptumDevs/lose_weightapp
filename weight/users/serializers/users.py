"""Users Serializers."""

# Django
from django.contrib.auth import password_validation, authenticate
from django.conf import settings

# Django Rest Framework
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework.authtoken.models import Token

# Model
from weight.users.models import User

# Serializers
from weight.users.serializers.profiles import ProfileModelSerializer


class UserModelSerializer(serializers.ModelSerializer):
    """User model serializer."""

    profile = ProfileModelSerializer(read_only=True)

    class Meta:
        """Meta serializer."""

        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'profile'
        )


class UserLoginSerializer(serializers.Serializer):
    """Users login Serializer.

    Handle login request data.
    """

    email = serializers.EmailField()
    password = serializers.CharField(min_length=8)

    def validate(self, data):
        """Check credentials."""
        user = authenticate(username=data['email'], password=data['password'])
        if not user:
            raise serializers.ValidationError('Invalid credential')
        self.context['user'] = user
        return data

    def create(self, data):
        """Generate or retrieve new token."""
        # Token is one to one field with user
        token, created = Token.objects.get_or_create(user=self.context.get('user'))
        return self.context['user'], token.key