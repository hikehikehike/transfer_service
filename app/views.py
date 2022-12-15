from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import generic

from app.forms import ClientCreationFrom, OrderFrom
from app.models import Car, Client, Flight, Order


def index(request):
    car = Car.objects.count()
    client = Client.objects.count()
    flight = Flight.objects.all()

    context = {
        "car": car,
        "client": client,
        "flight": flight
    }

    return render(request, "app/index.html", context=context)


class FlightListViews(LoginRequiredMixin, generic.ListView):
    model = Flight
    fields = "__all__"


class CarListViews(LoginRequiredMixin, generic.ListView):
    model = Car
    fields = "__all__"


class FlightDetailViews(LoginRequiredMixin, generic.DetailView):
    model = Flight


class ClientCreation(generic.CreateView):
    model = Client
    form_class = ClientCreationFrom


@login_required
def order_creation(request, pk):

    if request.method == "POST":
        post_value = request.POST.copy()
        post_value["flight"] = pk
        post_value["client"] = request.user.id
        form = OrderFrom(post_value)
        if form.is_valid():

            form.save()
            return HttpResponseRedirect(reverse("app:thanks", args=[pk]))
    else:
        form = OrderFrom()

    flight = Flight.objects.get(pk=pk)
    context = {
            "form": form,
            "flight": flight
        }
    return render(
        request,
        "app/order_form.html",
        context=context
    )


def thanks(request, pk):
    order = Order.objects.filter(pk=pk)

    context = {
        "order": order
    }

    return render(request, "app/thanks.html", context=context)
