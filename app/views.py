from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import generic

from app.forms import ClientCreationFrom, OrderFrom
from app.models import Car, Client, Trip, Order


def index(request):
    car = Car.objects.count()
    client = Client.objects.count()
    order = Order.objects.count()
    trip = Trip.objects.all()

    context = {
        "car": car,
        "client": client,
        "trip": trip,
        "order": order
    }

    return render(request, "app/index.html", context=context)


class TripListViews(LoginRequiredMixin, generic.ListView):
    model = Trip
    fields = "__all__"


class CarListViews(LoginRequiredMixin, generic.ListView):
    model = Car
    fields = "__all__"


class TripDetailViews(LoginRequiredMixin, generic.DetailView):
    model = Trip


class ClientCreation(generic.CreateView):
    model = Client
    form_class = ClientCreationFrom


@login_required
def order_creation(request, pk):

    if request.method == "POST":
        post_value = request.POST.copy()
        post_value["trip"] = pk
        post_value["client"] = request.user.id
        form = OrderFrom(post_value)
        if form.is_valid():

            order = form.save()
            return HttpResponseRedirect(reverse("app:thanks", args=[order.pk]))
    else:
        form = OrderFrom()

    trip = Trip.objects.get(pk=pk)
    context = {
            "form": form,
            "trip": trip
        }
    return render(
        request,
        "app/order_form.html",
        context=context
    )


@login_required
def thanks(request, pk):
    order = Order.objects.get(pk=pk)
    context = {
        "order": order
    }

    return render(request, "app/thanks.html", context=context)
