from django.shortcuts import render, get_object_or_404
from .models import Product, Category

def product_lists(request):

    products = Product.objects.all()
    categories = Category.objects.all()
    top_level = Category.objects.filter(parent__isnull=True)

    context = {
        'products': products,
        'categories': categories,
        'top_level': top_level,
    }

    return render(request, 'products/product_lists.html', context)

def by_category(request, category_slug):

    category = get_object_or_404(Category, slug=category_slug)

    categories = Category.objects.all()
    products = Product.objects.all()

    children = Category.objects.filter(parent=category)
    top_level = Category.objects.filter(parent=None)

    context = {
        'category': category,
        'categories': categories,
        'products': products,
        'children': children,
        'top_level': top_level,

    }

    return render(request, 'products/category.html', context)