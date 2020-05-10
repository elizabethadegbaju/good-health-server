from django.contrib import admin

from .models import UserProfile, UserPost, EmergencyLine
# Register your models here.

admin.site.register(UserProfile)
admin.site.register(UserPost)
admin.site.register(EmergencyLine)
