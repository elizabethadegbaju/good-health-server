# Create your views here.
from django.contrib.auth.models import User
from rest_framework import viewsets

from .models import UserProfile, UserPost
from .serializers import UserProfileSerializer, UserPostSerializer, \
    UserSerializer


class UserProfileViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides `retrieve`, `create`, and `list` actions for a
    user profile object.
    """
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides `retrieve`, `create`, and `list` actions for a
    user object.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserPostViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides `retrieve`, `create`, and `list` actions for a
    post created by a user.
    """
    queryset = UserPost.objects.all()
    serializer_class = UserPostSerializer
