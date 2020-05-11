from django.contrib.auth.models import User
from rest_framework import serializers

from .models import UserProfile, UserPost, EmergencyLine


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for User Model.
    """

    class Meta:
        """
        UserSerializer Meta class.
        """
        model = User
        fields = ['url', 'first_name', 'last_name', 'email', 'password',
                  'is_staff', 'is_active', 'is_superuser']


class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for UserProfile Model.
    """

    class Meta:
        """
        UserProfileSerializer Meta class.
        """
        model = UserProfile
        fields = ['url', 'user']


class UserPostSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for UserPost Model.
    """

    class Meta:
        """
        UserPostSerializer Meta class.
        """
        model = UserPost
        fields = ['url', 'user', 'anonymous', 'location', 'created_at',
                  'updated_at', 'media1', 'media2', 'media3', 'extra']


class EmergencyLineSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for EmergencyLine Model.
    """
    class Meta:
        """
        EmergencyLineSerializer Meta class.
        """
        model = EmergencyLine
        field = ['name', 'phone_number']
