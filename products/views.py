from django.shortcuts import render, get_object_or_404
from .models import Product, Category, Brand

'''
View to render...something. Practice one. Delete? 
Currently what's under products/. Get rid of that page?
'''
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


'''
View to render the lists of products under each category
'''
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


'''
View to render the page for an individual product
'''
def single_product(request, category_slug, product_slug):

    products = Product.objects.all()
    this_product = get_object_or_404(Product, slug=product_slug)

    category = get_object_or_404(Category, slug=category_slug)

    this_brand = this_product.brand
    related_products = Product.objects.filter(
        categories__in=this_product.categories.all()).order_by('?')[:4]

    context = {
        'products': products,
        'this_product': this_product,
        'category': category,
        'this_brand': this_brand,
        'related_products': related_products,
    }

    return render(request, 'products/product.html', context)



