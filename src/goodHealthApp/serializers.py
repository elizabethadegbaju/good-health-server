from django.contrib.auth.models import User
from rest_framework import serializers

from .models import UserProfile, UserPost


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for User Model."""

    class Meta:
        """Meta class for UserSerializer."""
        model = User
        fields = ['url', 'first_name', 'last_name', 'email', 'password',
                  'is_staff', 'is_active', 'is_superuser']


class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for UserProfile Model."""

    class Meta:
        """Meta class for UserProfileSerializer."""
        model = UserProfile
        fields = ['url', 'user']


class UserPostSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for UserPost Model."""

    class Meta:
        """Meta class for UserPostSerializer."""
        model = UserPost
        fields = ['url', 'user', 'anonymous', 'location', 'created_at',
                  'updated_at', 'media1', 'media2', 'media3', 'extra']
