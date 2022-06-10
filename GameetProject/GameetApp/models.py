from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User



# Create your models here.

class Usuario(models.Model):
    user =  models.OneToOneField(User, on_delete=models.CASCADE)
    tlf = PhoneNumberField(unique = True)
    imagen = models.ImageField(upload_to='imagenesPerfil')