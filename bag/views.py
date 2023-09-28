from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from products.models import Product


def view_bag(request):
    '''
    A view to render the shopping bag/basket page
    '''
    return render(request, 'bag/bag.html')


def add_to_bag(request, product_id):
    '''
    A view to add items to the shopping bag/basket
    Copied and modified from Boutique Ado
    '''
    product = get_object_or_404(Product, pk=product_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')

    '''
    Fetches bag from session or creates new bag dict
    if there wasn't one there before
    '''
    bag = request.session.get('bag', {})

    if product_id in bag:
        bag[product_id] += quantity
        messages.success(request,
                         f'Updated {product.name} to {bag[product_id]}')
    else:
        bag[product_id] = quantity
        messages.success(request,
                         f'Added {product.name} x {quantity} to your basket')

    '''
    Adds the bag back to the session in case it wasn't there before
    '''
    request.session['bag'] = bag

    return redirect(redirect_url)


def edit_bag(request, product_id):
    '''
    Adjusts the quantity of the selected product to the specified amount
    Copied and modified from Boutique Ado
    '''

    product = get_object_or_404(Product,
                                pk=product_id)
    quantity = int(request.POST.get('quantity'))

    bag = request.session.get('bag', {})

    if quantity == 0 or "remove" in request.POST:
        bag.pop(product_id)
        messages.success(request, f'Removed {product.name} from your bag')
    else:
        bag[product_id] = quantity
        messages.success(request,
                         f'Updated {product.name} to {bag[product_id]}')

    request.session['bag'] = bag
    return redirect(reverse('view-bag'))
