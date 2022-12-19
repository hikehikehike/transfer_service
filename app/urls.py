from django.urls import path

from app.views import (
    index,
    TripListViews,
    CarListViews,
    TripDetailViews,
    ClientCreation,
    order_creation,
    thanks
)

urlpatterns = [
    path("", index, name="index"),
    path("trip/", TripListViews.as_view(), name="trip-list"),
    path("car/", CarListViews.as_view(), name="car-list"),
    path("trip/<int:pk>/", TripDetailViews.as_view(), name="trip-detail"),
    path("trip/<int:pk>/order/", order_creation, name="order-creation"),
    path("client/creation", ClientCreation.as_view(), name="client-creation"),
    path("thanks/<int:pk>", thanks, name="thanks")
]


app_name = "app"
