from django import forms

from app.models import Order, Client


class ClientForm(forms.ModelForm):

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
