from datetime import datetime

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from app.forms import OrderFrom, ClientCreationFrom
from app.models import Trip, Car, Order


class TestPublic(TestCase):
    def test_index(self):
        response = self.client.get(reverse("app:index"))

        self.assertEqual(response.status_code, 200)

    def test_trip_list(self):
        response = self.client.get(reverse("app:trip-list"))

        self.assertNotEqual(response.status_code, 200)

    def test_trip_detail(self):
        response = self.client.get(reverse("app:trip-detail", args="2"))

        self.assertNotEqual(response.status_code, 200)

    def test_car(self):
        response = self.client.get(reverse("app:car-list"))

        self.assertNotEqual(response.status_code, 200)

    def test_order(self):
        response = self.client.get(reverse("app:order-creation", args="2"))

        self.assertNotEqual(response.status_code, 200)

    def test_thanks(self):
        response = self.client.get(reverse("app:thanks", args="2"))

        self.assertNotEqual(response.status_code, 200)


class TestPrivate(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="admin",
            password="admin12345"
        )

        self.client.force_login(self.user)

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
        order = Order.objects.create(
            trip=trip,
            date_trip=datetime(2022, 10, 8),
            number_of_seat=2,
            client=self.user
        )

    def test_index(self):
        response = self.client.get(reverse("app:index"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "app/index.html")

    def test_trip_list(self):
        response = self.client.get(reverse("app:trip-list"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "app/trip_list.html")

    def test_trip_detail(self):
        response = self.client.get(reverse("app:trip-detail", args="1"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "app/trip_detail.html")

    def test_car(self):
        response = self.client.get(reverse("app:car-list"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "app/car_list.html")

    def test_order(self):
        response = self.client.get(reverse("app:order-creation", args="1"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "app/order_form.html")

    def test_thanks(self):
        response = self.client.get(reverse("app:thanks", args="1"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "app/thanks.html")


class TestPost(TestCase):
    def test_creation_order(self):
        self.user = get_user_model().objects.create_user(
            username="admin",
            password="admin12345"
        )

        self.client.force_login(self.user)

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

        form_data = {
            "trip": trip.pk,
            "date_trip": datetime(2022, 10, 8),
            "number_of_seat": 1,
            "client": self.user.pk
        }

        form = OrderFrom(data=form_data)
        self.assertTrue(form.is_valid())

    def test_client_creation(self):
        form_data = {
            "name": "Timur",
            "phone_number": 911,
            "password1": "admin1234test",
            "password2": "admin1234test"
        }

        form = ClientCreationFrom(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)
