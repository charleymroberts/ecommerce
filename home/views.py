from django.shortcuts import render
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

def privacy(request):
    '''
    A view to render the privacy policy page
    '''

    return render(request, 'home/privacy.html')


def terms(request):
    '''
    A view to render the terms page
    '''

    return render(request, 'home/terms.html')


def delivery(request):
    '''
    A view to render the delivery page
    '''

    return render(request, 'home/delivery.html')


def contact(request):
    '''
    A view to render the contact page
    '''

    return render(request, 'home/contact.html')