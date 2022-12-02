from django.contrib.auth.models import AbstractUser
from django.db import models


class Car(models.Model):
    name = models.CharField(max_length=255, default="Car")
    capacity = models.IntegerField()
    comfort = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}. Capacity: {self.capacity}. Comfort: {self.comfort}"


class Flight(models.Model):
    name = models.CharField(max_length=255)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    cost = models.IntegerField()
    car = models.ForeignKey(Car, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}. Travel time:{self.arrival_time - self.departure_time}"


class Client(AbstractUser):
    name = models.CharField(max_length=255)
    phone_number = models.IntegerField(null=True, blank=True)
    flight = models.ManyToManyField(Flight, related_name="client")
