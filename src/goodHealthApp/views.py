# Create your views here.
from django.contrib.auth.models import User
from rest_framework import viewsets

from .models import UserProfile, UserPost
from .serializers import UserProfileSerializer, UserPostSerializer, UserSerializer


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserPostViewSet(viewsets.ModelViewSet):
    queryset = UserPost.objects.all()
    serializer_class = UserPostSerializer
