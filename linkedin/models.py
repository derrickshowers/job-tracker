from django.db import models
from django.contrib.auth.models import User

# TODO: LinkedIn should go to Linkedin
class LinkedInUser(models.Model):
    user = models.OneToOneField(User)
    access_token = models.CharField(max_length=200)

    def __str__(self):
        return self.user.username

    @classmethod
    def addToken(cls, user, token):
        try:
            currentUser = cls.objects.get(user=user)
            currentUser.access_token = token
        except:
            currentUser = cls(user=user, access_token=token)
        currentUser.save()


