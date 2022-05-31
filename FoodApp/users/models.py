from email.policy import default
from django.db import models
from django.contrib.auth.models import User # imported user (remember usercreation form)
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) #linked to user account
    image = models.ImageField(default='profile.png', upload_to = 'image_dir')
    location = models.CharField(max_length=500)

    def __str__(self):
        return self.user.username