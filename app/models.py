from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.db.models import DateTimeField
from phonenumber_field.modelfields import PhoneNumberField


class DateTimeWithoutTZField(DateTimeField):
    def db_type(self, connection):
        return 'timestamp'


class Car(models.Model):
    name = models.CharField(max_length=255, default="Car")
    capacity = models.IntegerField()
    comfort = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}. Capacity: {self.capacity}. Comfort: {self.comfort}"


class Trip(models.Model):
    name = models.CharField(max_length=255)
    departure_time = DateTimeWithoutTZField()
    arrival_time = DateTimeWithoutTZField()
    cost = models.IntegerField()
    car = models.ForeignKey(Car, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}. Travel time:{self.arrival_time - self.departure_time}"


class Client(AbstractUser):
    name = models.CharField(max_length=255)
    phone_number = PhoneNumberField(null=False, blank=False, unique=True)

    def save(self, *args, **kwargs):
        self.username = self.phone_number
        super(Client, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("login")


class Order(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    date_trip = DateTimeWithoutTZField()
    number_of_seat = models.IntegerField(default=1)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
