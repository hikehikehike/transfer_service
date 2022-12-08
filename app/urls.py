from django.urls import path

from app.views import index, FlightListViews, CarListViews, FlightDetailViews, order_flight_views

urlpatterns = [
    path("", index, name="index"),
    path("flight/", FlightListViews.as_view(), name="flight-list"),
    path("car/", CarListViews.as_view(), name="car-list"),
    path("flight/<int:pk>/", FlightDetailViews.as_view(), name="flight-detail"),
    path("flight/<int:pk>/order", order_flight_views, name="flight-order")
]


app_name = "app"
