from django.urls import path, include
from rest_framework import routers

from .views import UserPostViewSet, UserProfileViewSet, UserViewSet

router = routers.DefaultRouter()
router.register(r'userprofiles', UserProfileViewSet)
router.register(r'postfeed', UserPostViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
