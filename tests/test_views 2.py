from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


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

    def test_order_creation(self):
        response = self.client.get(reverse("app:order-creation", args="2"))

        self.assertNotEqual(response.status_code, 200)

    def test_thanks(self):
        response = self.client.get(reverse("app:thanks", args="2"))

        self.assertNotEqual(response.status_code, 200)


class TestIndexPrivate(TestCase):
    def setUp(self) -> None:
        self.client.force_login(get_user_model().objects.get(id=0))

    def test_index(self):
        response = self.client.get(reverse("app:index"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "app/index.html")

