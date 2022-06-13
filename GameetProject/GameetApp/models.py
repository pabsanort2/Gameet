from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User



# Create your models here.
class GameetUser(models.Model):
    user =  models.OneToOneField(User, on_delete=models.CASCADE)
    telephone = PhoneNumberField(unique = True)
    picture = models.ImageField(upload_to='profilePictures')