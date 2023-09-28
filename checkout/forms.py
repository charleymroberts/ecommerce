from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = (
            "email",
            "full_name",
            "line_one",
            "line_two",
            "line_three",
            "town_city_or_area",
            "county",
            "postcode",
        )

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            "full_name": "Full Name",
            "email": "Email Address",
            "line_one": "Street Address 1",
            "line_two": "Street Address 2",
            "line_three": "Street Address 3",
            "town_city_or_area": "Town, City or Area",
            "postcode": "Postcode",
            "county": "County",
        }

        self.fields["full_name"].widget.attrs["autofocus"] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f"{placeholders[field]} *"
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs["placeholder"] = placeholder
            # self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            # self.fields[field].label = ""
