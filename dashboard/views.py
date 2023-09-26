from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from .forms import ProductForm, BrandForm
from products.models import Product, Brand


# All views on this page are for functionality only available to store owners

# Create your views here.
@login_required()
@permission_required('products.view_product', raise_exception=True)
def dashboard(request):
    '''
    A view to render the store owner's admin dashboard
    '''

    return render(request, 'dashboard/dashboard.html')


@login_required()
@permission_required('products.add_product', raise_exception=True)
def add_product(request):
    '''
    A view to render the 'Add product' form
    '''
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product added successfully')
            return redirect('dashboard')
    form = ProductForm()
    context = {
        'form': form,
    }

    return render(request, 'dashboard/add-product.html', context)


@login_required()
@permission_required('products.view_product', raise_exception=True)
def view_products(request):
    '''
    Displays a list of all products in alphabetical order
    '''
    products = Product.objects.all().order_by('name')

    context = {
        'products': products,
    }

    return render(request, 'dashboard/view-products.html', context)


@login_required()
@permission_required('products.change_product', raise_exception=True)
def edit_product(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, "Product edited successfully")
            return redirect('view-products')
    form = ProductForm(instance=product)
    context = {
        'form': form,
        'product': product,
    }

    return render(request, 'dashboard/edit-product.html', context)


@login_required()
@permission_required('products.add_brand', raise_exception=True)
def add_brand(request):
    '''
    A view to render the 'Add brand' form
    '''
    if request.method == 'POST':
        form = BrandForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Brand added successfully')
            return redirect('dashboard')
    form = BrandForm()
    context = {
        'form': form,
    }

    return render(request, 'dashboard/add-brand.html', context)


@login_required()
@permission_required('products.change_brand', raise_exception=True)
def edit_brand(request, brand_slug):
    '''
    View to render the 'edit brand' form
    '''
    brand = get_object_or_404(Brand, slug=brand_slug)
    if request.method == 'POST':
        form = BrandForm(request.POST, instance=brand)
        if form.is_valid():
            form.save()
            messages.success(request, "Brand edited successfully")
            return redirect('dashboard')
    form = BrandForm(instance=brand)
    context = {
        'form': form,
        'brand': brand,
    }

    return render(request, 'dashboard/edit-brand.html', context)


@login_required()
@permission_required('products.view_brand', raise_exception=True)
def view_brands(request):
    '''
    Displays a list of all brands in alphabetical order
    '''
    brands = Brand.objects.all().order_by('name')

    context = {
        'brands': brands,
    }

    return render(request, 'dashboard/view-brands.html', context)