from django.urls import path

from app.views import index, FlightListViews, CarListViews

urlpatterns = [
    path("", index, name="index"),
    path("flight/", FlightListViews.as_view(), name="flight-list"),
    path("car/", CarListViews.as_view(), name="car-list"),
]


app_name = "app"
