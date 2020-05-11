from django.urls import path, include
from rest_framework import routers

from .views import UserPostViewSet, UserProfileViewSet, UserViewSet, \
    EmergencyLineViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'userprofiles', UserProfileViewSet)
router.register(r'postfeed', UserPostViewSet)
router.register(r'users', UserViewSet)
router.register(r'emergencylines', EmergencyLineViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
