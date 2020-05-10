from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now


class UserProfile(models.Model):
    """
    UserProfile Model.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # TODO(Idowu is to create user but UserPost is linked to it so here is a
    #  dummy model for me to use)


def get_upload_path(instance, filename):
    year = now().year
    month = now().month
    day = now().day
    return 'uploads/{0}/{1}/{2}/'.format(year, month, day) + filename


class UserPost(models.Model):
    """
    UserPost Model for each post created by a user.

    It can be an anonymous post without extra information. Only one media
    file is required when creating a post and the time is stamped at the
    point of creating the record.
    """
    user = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True,
                             blank=True)
    anonymous = models.BooleanField(default=True)
    media1 = models.FileField(upload_to=get_upload_path)
    media2 = models.FileField(upload_to=get_upload_path, null=True, blank=True)
    media3 = models.FileField(upload_to=get_upload_path, null=True, blank=True)
    location = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    extra = models.TextField(blank=True)

    class Meta:
        """
        UserPost Meta class.
        """
        ordering = ['-created_at']

    def __str__(self):
        """
        Converts  UserPost object to a string.

        :returns: the users name and time of post
        :rtype: string
        """
        if self.user == None:
            user = "user_not_found"
        else:
            user = str(self.user)
        return user + " - " + str(self.created_at)



#ADEMOLA - EmergencyLine Model
class EmergencyLine(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.IntegerField()

    #property
    def __str__(self):
        return self.name
