from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now


class UserProfile(models.Model):
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
    UserPost represents a user post in our system. It can be an anonymous post
    without extra information. Only one media file is required when
    creating a post and the time is stamped at the point of creating the record.
    """
    user = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True,
                             blank=True)
    anonymous = models.BooleanField(default=True)
    media1 = models.FileField(upload_to=get_upload_path)
    media2 = models.FileField(upload_to=get_upload_path, null=True, blank=True)
    media3 = models.FileField(upload_to=get_upload_path, null=True, blank=True)
    location = models.CharField(max_length=30)
    time = models.DateTimeField(auto_now_add=True)
    extra = models.TextField(null=True, blank=True)

    class Meta:
        """

        """
        ordering = ['time']

    def __str__(self):
        """
        returns the users name and time of post
        :return: string
        """
        if self.user == None:
            user = "user_not_found"
        else:
            user = str(self.user)
        return user + " - " + str(self.time)
