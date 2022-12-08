from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from app.forms import ClientForm, OrderFrom
from app.models import Car, Client, Flight, Order


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


class FlightDetailViews(generic.DetailView):
    model = Flight


# class OrderFlightViews(generic.CreateView):
#     model = Order
#     fields = "__all__"
    # success_url = reverse_lazy("app:thanks")

def order_flight_views(request, pk):
    flight = Flight.objects.get(pk=pk)

    context = {
        "flight": flight
    }

    form_client = ClientForm(request.POST or None)
    if form_client.is_valid():
        if Client.objects.filter(phone_number=form_client.cleaned_data["phone_number"]).first():
            form_client = Client.objects.filter(phone_number=form_client.cleaned_data["phone_number"])
        else:
            form_client.save()
    context["form_client"] = form_client

    initial_dict = {
        "flight": flight,
        "client": form_client
    }

    form_order = OrderFrom(request.POST or None, initial=initial_dict)
    if form_order.is_valid():
        form_order.save()

    context["form_order"] = form_order

    return render(request, "app/order_form.html", context=context)
