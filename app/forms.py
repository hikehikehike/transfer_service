from django.contrib.auth.forms import UserCreationForm
from django import forms

from app.models import Client, Order


class ClientCreationFrom(UserCreationForm):

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
            "flight",
            "date_flight",
            "number_of_seat",
            "client"
        ]
        widgets = {
            "flight": forms.HiddenInput(),
            "client": forms.HiddenInput()
        }