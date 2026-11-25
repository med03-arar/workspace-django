from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass

class Doctor(User):
    licence_number= models.CharField(max_length=6,unique=True)
    phone= models.CharField(max_length=8)
    specialities= models.ManyToManyField('Speciality', related_name='doctors', null=True, blank=True)
class Patient(User):
    national_id= models.CharField(max_length=8,unique=True)
    phone= models.CharField(max_length=8)
    birth_date= models.DateField()

class Speciality(models.Model):
    name= models.CharField(max_length=50)
