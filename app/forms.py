from django import forms
from django.contrib.auth.forms import UserCreationForm

from app.models import Order, Client


class ClientForm(UserCreationForm):

    class Meta:

        model = Client

        fields = [
            "name",
            "phone_number",
        ]


class OrderFrom(forms.ModelForm):

    class Meta:

        model = Order

        fields = [
            "date_flight",
            "number_of_seat",
        ]
