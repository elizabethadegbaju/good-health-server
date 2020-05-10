# Create your views here.
from django.contrib.auth.models import User
from rest_framework import viewsets

<<<<<<< HEAD
from .models import UserProfile, UserPost, EmergencyLine
from .serializers import UserProfileSerializer, UserPostSerializer, \
    UserSerializer, EmergencyLineSerializer
=======
from .models import UserProfile, UserPost
from .serializers import UserProfileSerializer, UserPostSerializer, \
    UserSerializer
>>>>>>> develop


class UserProfileViewSet(viewsets.ModelViewSet):
    """
    userprofile viewset that provides `retrieve`, `create`, and `list` actions.
    """
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    user viewset that provides `retrieve`, `create`, and `list` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserPostViewSet(viewsets.ModelViewSet):
    """
    userpost viewset that provides `retrieve`, `create`, and `list` actions.
    """
    queryset = UserPost.objects.all()
    serializer_class = UserPostSerializer
<<<<<<< HEAD


# emergencyline viewset
class EmergencyLineViewset(viewsets.ModelViewSet):
    """
    emergencyline viewset that provides 'retrieve', 'create', and 'list' actions.
    """
    queryset = EmergencyLine.objects.all()
    serializer_class = EmergencyLineSerializer
    
=======
>>>>>>> develop
