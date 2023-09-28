from django import forms

from products.models import Product, Brand


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = [
            'name',
            'brand',
            'slug',
            'image',
            'wholesale_price',
            'retail_price',
            'vat_rate',
            'barcode',
            'ingredients',
            'nutrition_info',
            'description',
            'is_organic',
            'is_glutenfree',
            'categories',
        ]


class BrandForm(forms.ModelForm):

    class Meta:
        model = Brand
        fields = [
            'name',
            'slug',
            'description',
        ]
