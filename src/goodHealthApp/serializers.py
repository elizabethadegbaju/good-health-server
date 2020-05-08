from django.contrib.auth.models import User
from rest_framework import serializers

from .models import UserProfile, UserPost


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        """

        """
        model = User
        fields = ['url', 'first_name', 'last_name', 'email', 'password',
                  'is_staff', 'is_active', 'is_superuser']


class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        """

        """
        model = UserProfile
        fields = ['url', 'user']


class UserPostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        """

        """
        model = UserPost
        fields = ['url', 'user', 'anonymous', 'location', 'time', 'media1',
                  'media2', 'media3', 'extra']
