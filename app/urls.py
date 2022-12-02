from django.urls import path

from app.views import index, FlightListViews

urlpatterns = [
    path("", index, name="index"),
    path("flight/", FlightListViews.as_view(), name="flight-list"),

]


app_name = "app"
