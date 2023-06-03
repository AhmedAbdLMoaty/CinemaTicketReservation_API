from django.db import models

# Create your models here.

class Movie(models.Model):
    hall = models.CharField(max_length=10, )
    movie = models.CharField(max_length=10,)
    date = models.DateField()
    time = models.TimeField()

class Guest(models.Model):
    name = models.CharField(max_length=30, null= False)
    mobile = models.CharField(max_length=15)

class Reservation(models.Model):
    guest = models.ForeignKey(Guest, related_name='reservation', on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, related_name='reservation', on_delete=models.CASCADE)