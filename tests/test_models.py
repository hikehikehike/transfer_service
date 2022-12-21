from django.test import TestCase

from app.models import Car


class ModelsTests(TestCase):
    def test_car_str(self):
        car = Car.objects.create(
            name="Ford",
            capacity="5",
            comfort="Conditioner"
        )
        self.assertEqual(str(car), car.name)
        