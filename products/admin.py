from django.contrib import admin
from .models import Product, Category, Brand


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'parent',
        'description',
        'slug',
    )


class BrandAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
        'slug',
    )


class ProductAdmin(admin.ModelAdmin):
    list_display = (
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
    )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Product, ProductAdmin)
