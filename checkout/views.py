from django.shortcuts import (
    render,
    redirect,
    reverse,
    get_object_or_404,
    HttpResponse,
)
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from .models import Order, OrderLineItem

from products.models import Product
from profiles.models import ShippingAddress
from bag.contexts import bag_contents

import stripe
import json


@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get("client_secret").split("_secret")[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(
            pid,
            metadata={
                "bag": json.dumps(request.session.get("bag", {})),
                "save_info": request.POST.get("save_info"),
                "username": request.user,
            },
        )
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(
            request,
            (
                "Sorry, your payment cannot be "
                "processed right now. Please try "
                "again later."
            ),
        )
        return HttpResponse(content=e, status=400)


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == "POST":
        bag = request.session.get("bag", {})

        form_data = {
            "full_name": request.POST["full_name"],
            "email": request.POST["email"],
            "line_one": request.POST["line_one"],
            "line_two": request.POST["line_two"],
            "line_three": request.POST["line_three"],
            "town_city_or_area": request.POST["town_city_or_area"],
            "postcode": request.POST["postcode"],
            "county": request.POST["county"],
        }

        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            pid = request.POST.get("client_secret").split("_secret")[0]
            order.stripe_pid = pid
            order.original_bag = json.dumps(bag)
            order.save()

            for item_id, quantity in bag.items():
                try:
                    product = Product.objects.get(id=item_id)
                    if product.categories.filter(
                        parent__slug="chilled"
                    ).exists():
                        order.cool_box_included = True
                        order.save()
                    order_line_item = OrderLineItem(
                        order=order,
                        product=product,
                        quantity=quantity,
                    )
                    order_line_item.save()
                except Product.DoesNotExist:
                    messages.error(
                        request,
                        (
                            "One of the products in your bag wasn't "
                            "found in our database. "
                            "Please contact us for assistance!"
                        ),
                    )
                    order.delete()
                    return redirect(reverse("view_bag"))

            # Save the info to the user's profile if all is well
            request.session["save_info"] = "save-info" in request.POST
            return redirect(
                reverse("checkout_success", args=[order.order_number])
            )
        else:
            messages.error(
                request,
                (
                    "There was an error with your form. "
                    "Please double check your information."
                ),
            )
    else:
        bag = request.session.get("bag", {})
        if not bag:
            messages.error(
                request, "There's nothing in your bag at the moment"
            )
            return redirect(reverse("products"))

        current_bag = bag_contents(request)
        total = current_bag["grand_total"]
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        # Attempt to prefill the form a default shipping address
        # if the user has one
        if request.user.is_authenticated:
            default_address = ShippingAddress.objects.filter(
                user=request.user, default_address=True
            ).first()
            if default_address:
                order_form = OrderForm(
                    initial={
                        "full_name": default_address.full_name,
                        "email": request.user.email,
                        "line_one": default_address.line_one,
                        "line_two": default_address.line_two,
                        "line_three": default_address.line_three,
                        "town_city_or_area": default_address.town_city_or_area,
                        "county": default_address.county,
                        "postcode": default_address.postcode,
                    }
                )
            else:
                order_form = OrderForm(
                    initial={
                        "email": request.user.email,
                    }
                )
            user_addresses = ShippingAddress.objects.filter(user=request.user)
        else:
            order_form = OrderForm()
            user_addresses = []

    if not stripe_public_key:
        messages.warning(
            request,
            (
                "Stripe public key is missing. "
                "Did you forget to set it in "
                "your environment?"
            ),
        )

    template = "checkout/checkout.html"
    context = {
        "user_addresses": user_addresses,
        "order_form": order_form,
        "stripe_public_key": stripe_public_key,
        "client_secret": intent.client_secret,
    }

    return render(request, template, context)


def checkout_success(request, order_number):
    """
    Handle successful checkouts
    """
    order = get_object_or_404(Order, order_number=order_number)

    if request.user.is_authenticated:
        # Attach the user's profile to the order
        order.user = request.user
        order.save()

    messages.success(
        request,
        f"Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.",
    )

    if "bag" in request.session:
        del request.session["bag"]

    template = "checkout/checkout_success.html"
    context = {
        "order": order,
    }

    return render(request, template, context)
