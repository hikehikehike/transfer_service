from django.contrib.auth.models import AbstractUser
from django.db import models


class Car(models.Model):
    capacity = models.CharField(max_length=255)
    comfort = models.CharField(max_length=255)


class Flight(models.Model):
    name = models.CharField(max_length=255)
    departure_time = models.TimeField()
    arrival_time = models.TimeField()
    cost = models.IntegerField()
    car = models.ForeignKey(Car, on_delete=models.CASCADE)


class Client(AbstractUser):
    name = models.CharField(max_length=255)
    phone_number = models.IntegerField()
    flight = models.ManyToManyField(Flight, related_name="client")
