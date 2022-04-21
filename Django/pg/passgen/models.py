from django.db import models

# Create your models here.

class Booking(models.Model):
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    countParticipant = models.IntegerField(max_length=1)
    purpose = models.CharField(max_length=255)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.IntegerField(max_length=11)
    comments = models.TextField(blank=True)