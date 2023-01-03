from django.contrib.auth.forms import UserCreationForm
from django import forms
from phonenumber_field.formfields import PhoneNumberField

from app.models import Client, Order


class ClientCreationFrom(UserCreationForm):
    phone_number = PhoneNumberField(region="UA")

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
            "trip",
            "date_trip",
            "number_of_seat",
            "client"
        ]
        widgets = {
            "trip": forms.HiddenInput(),
            "client": forms.HiddenInput()
        }
