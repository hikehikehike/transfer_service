from django.urls import path

from app.views import IndexViews, index

urlpatterns = [
    path("", index, name="index")
]


app_name = "app"
