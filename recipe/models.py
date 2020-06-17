from django.db import models
from django.contrib.auth.models import User
import datetime as dt
from cloudinary.models import CloudinaryField

# Create your models here.

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic = CloudinaryField('profile_pic')
    bio=models.CharField(max_length = 100)
    contacts=models.CharField(max_length = 100)

    def __str__(self):
        return self.user 

    @classmethod
    def save_profile(self):
        self.save()

    @classmethod
    def delete_profile(self):
        self.delete() 

    @classmethod
    def update_profile(self):
        self.update()  