from django import forms

from .models import ShippingAddress


class AddressForm(forms.ModelForm):

    class Meta:
        model = ShippingAddress
        fields = [
            'line_one',
            'line_two',
            'line_three',
            'town_city_or_area',
            'county',
            'postcode',
        ]