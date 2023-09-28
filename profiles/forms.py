from django import forms

from .models import ShippingAddress


class AddressForm(forms.ModelForm):

    class Meta:
        model = ShippingAddress
        fields = [
            'full_name',
            'line_one',
            'line_two',
            'line_three',
            'town_city_or_area',
            'county',
            'postcode',
        ]

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Name',
            'line_one': 'Street Address 1',
            'line_two': 'Street Address 2',
            'line_three': 'Street Address 3',
            'town_city_or_area': 'Town, City or Area',
            'postcode': 'Postcode',
            'county': 'County',
        }

        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = ""
