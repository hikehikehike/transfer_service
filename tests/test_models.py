from datetime import datetime

from django.test import TestCase

from app.models import Car, Trip, Client


class ModelsTests(TestCase):
    def test_car_str(self):
        car = Car.objects.create(
            name="Ford",
            capacity="5",
            comfort="Conditioner"
        )
        self.assertEqual(
            str(car),
            f"{car.name}. Capacity: {car.capacity}. Comfort: {car.comfort}")

    def test_trip_str(self):
        car = Car.objects.create(
            name="Ford",
            capacity="5",
            comfort="Conditioner"
        )
        trip = Trip.objects.create(
            name="Odessa - Simferopol",
            departure_time=datetime(2022, 10, 8),
            arrival_time=datetime(2023, 6, 20),
            cost="1",
            car=car
        )

        self.assertEqual(str(trip), f"{trip.name}. Travel time:{trip.arrival_time - trip.departure_time}")

    def test_create_client_with_name_and_phone_number(self):
        name = "Timur"
        username = "Naruto"
        phone_number = "911"
        password = "ZSU12345"

        client = Client.objects.create_user(
            username=username,
            name=name,
            phone_number=phone_number,
            password=password
        )

        self.assertEqual(client.name, name)
        self.assertEqual(client.phone_number, phone_number)
