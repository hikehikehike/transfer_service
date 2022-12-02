from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from app.models import Car, Client, Flight


def index(request):
    car = Car.objects.count()
    client = Client.objects.count()
    flight = Flight.objects.all()

    context ={
        "car": car,
        "client": client,
        "flight": flight
    }

    return render(request, "app/index.html", context=context)


class FlightListViews(generic.ListView):
    model = Flight
    fields = "__all__"


class CarListViews(generic.ListView):
    model = Car
    fields = "__all__"
