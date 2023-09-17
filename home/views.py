from django.shortcuts import render, get_object_or_404
from products.models import Category, Product

def index(request):
    """ a view to return the index page """

    products = Product.objects.all()
    new_products_category = Category.objects.get(slug='new-products')
    four_new_products = new_products_category.products.order_by('?')[:4]
    bestsellers_category = Category.objects.get(slug="bestsellers")
    four_random_bestsellers = bestsellers_category.products.order_by('?')[:4]

    context = {
        'products': products,
        'new_products': four_new_products,
        'bestseller_products': four_random_bestsellers,
    }

    return render(request, 'home/index.html', context)

