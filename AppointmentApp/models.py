from django.db import models

# Create your models here.
class Status(models.TextChoices):
    PENDING = 'Pending', 'Pending'
    CONFIRMED = 'Confirmed', 'Confirmed'
    CANCELLED = 'Cancelled', 'Cancelled'
    
class Appointment(models.Model):
    Status= models.CharField(max_length=20, choices=Status.choices, default=Status.PENDING)
    reason= models.TextField()
    duration_minute= models.IntegerField()
    appointement_date=models.DateTimeField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt= models.DateTimeField(auto_now=True)
    doctor= models.ForeignKey('AccountApp.Doctor', on_delete=models.CASCADE,null=True, blank=True)
    patient= models.ForeignKey('AccountApp.Patient', on_delete=models.CASCADE,null=True, blank=True)