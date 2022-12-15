from django.urls import path

from app.views import (
    index,
    FlightListViews,
    CarListViews,
    FlightDetailViews,
    ClientCreation,
    order_creation,
    thanks
)

urlpatterns = [
    path("", index, name="index"),
    path("flight/", FlightListViews.as_view(), name="flight-list"),
    path("car/", CarListViews.as_view(), name="car-list"),
    path("flight/<int:pk>/", FlightDetailViews.as_view(), name="flight-detail"),
    path("flight/<int:pk>/order/", order_creation, name="order-creation"),
    path("client/creation", ClientCreation.as_view(), name="client-creation"),
    path("thanks/<int:pk>", thanks, name="thanks")
]


app_name = "app"
