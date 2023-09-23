from django.shortcuts import render, redirect, reverse, HttpResponse, \
    get_object_or_404
from django.contrib import messages
from products.models import Product


# Create your views here.
def view_bag(request):
    '''
    A view to render the shopping bag/basket page
    '''
    return render(request, 'bag/bag.html')


def add_to_bag(request, product_id):
    '''
    A view to add items to the shopping bag/basket
    '''
    product = get_object_or_404(Product, pk=product_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')

    bag = request.session.get('bag', {}) # Fetches bag from session or creates \
                                        # new bag dict if there wasn't one there before

    if product_id in bag:
        bag[product_id] += quantity
        messages.success(request, f'Updated {product.name} to {bag[product_id]}')
    else:
        bag[product_id] = quantity
        messages.success(request, f'Added {product.name} x {quantity} to your basket')

    request.session['bag'] = bag # Adds the bag back to the session \
                                 # in case it wasn't there before
    return redirect(redirect_url)


def edit_bag(request, product_id):
    """ Adjust the quantity of the specified product to the specified amount """

    product = get_object_or_404(Product,
                                pk=product_id)
    quantity = int(request.POST.get('quantity'))

    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[product_id] = quantity
        messages.success(request,
                         f'Updated {product.name} to {bag[product_id]}')
    else:
        bag.pop(item_id)
        messages.success(request, f'Removed {product.name} from your basket')

    request.session['bag'] = bag
    return redirect(reverse('view-bag'))


def remove_from_bag(request, product_id):
    """ Remove the item from the shopping bag """

    try:
        product = get_object_or_404(Product, pk=product_id)
        bag = request.session.get('bag', {})

        bag.pop(product_id)
        messages.success(request, f'Removed {product.name} from your basket')

        request.session['bag'] = bag
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)

