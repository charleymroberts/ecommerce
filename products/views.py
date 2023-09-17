from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from .models import Product, Category, Brand
from django.db.models import Q

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

    products = Product.objects.filter(
        Q(categories=category) | Q(categories__parent=category)
    )

    products = products.order_by('name')

    children = Category.objects.filter(parent=category)
    top_level = Category.objects.filter(parent=None)

    sortkey = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
        products = products.order_by(sortkey)

    context = {
        'category': category,
        'categories': categories,
        'products': products,
        'children': children,
        'top_level': top_level,
        'sortkey': sortkey,

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


def brand(request, brand_slug):
    '''
    View to render a page containing brand info and a list of products by that brand
    '''
    current_brand = get_object_or_404(Brand, slug=brand_slug)
    products = current_brand.product_set.all()
    products = products.order_by('name')


    brands = Brand.objects.all()

    categories = Category.objects.all()

    products_by_brand = Product.objects.filter(brand=current_brand)

    sortkey = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
        products = products.order_by(sortkey)

    context = {
        'current_brand': current_brand,
        'products': products,
        'brands': brands,
        'categories': categories,
        'products_by_brand': products_by_brand,
        'sortkey': sortkey,
    }

    return render(request, 'products/brand.html', context)


def search_results(request):

    products = Product.objects.all()
    # category = get_object_or_404(Category, slug=category_slug)

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                # return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    context = {
        'query': query,
        'products': products,
    }

    return render(request, 'products/search.html', context)