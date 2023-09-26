from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


'''
This file copied from Boutique Ado walkthrough project (with references
to sizes removed as they are not needed for this project)
'''
def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})
    has_chilled = False

    for product_id, quantity in bag.items():
        product = get_object_or_404(Product, pk=product_id)
        total += quantity * product.retail_price
        product_count += quantity
        '''
        checks if any of the products are in the chilled category
        e.g. can use this information to only display the next-day delivery 
        option on the basket page if the basket contains any chilled products
        '''
        if product.categories.filter(parent__slug='chilled').exists():
            has_chilled = True
        bag_items.append({
            'product_id': product_id,
            'quantity': quantity,
            'product': product,
        })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = 5
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    chilled_total = total + settings.COOL_BOX

    grand_total = delivery + total
    if has_chilled:
        grand_total += settings.COOL_BOX

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'has_chilled': has_chilled,
        'cool_box': settings.COOL_BOX,
        'chilled_total': chilled_total,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,

    }

    return context