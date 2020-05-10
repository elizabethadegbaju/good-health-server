from django.urls import path, include
from rest_framework import routers

<<<<<<< HEAD
from .views import UserPostViewSet, UserProfileViewSet, UserViewSet, EmergencyLineViewSet
=======
from .views import UserPostViewSet, UserProfileViewSet, UserViewSet
>>>>>>> develop

router = routers.DefaultRouter()
router.register(r'userprofiles', UserProfileViewSet)
router.register(r'postfeed', UserPostViewSet)
router.register(r'users', UserViewSet)
<<<<<<< HEAD
router.register(r'emergencyline', EmergencyLineViewSet)
=======
>>>>>>> develop

urlpatterns = [
    path('', include(router.urls)),
]
