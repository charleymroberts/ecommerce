from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import AddressForm
from .models import ShippingAddress
from checkout.models import Order


@login_required()
def my_account(request):
    """
    View to render the 'My Account' landing page
    """

    return render(request, "profiles/account.html")


@login_required()
def addresses(request):
    """
    View to render the add/edit shipping addresses page
    """
    user_addresses = ShippingAddress.objects.filter(user=request.user)

    context = {
        "user_addresses": user_addresses,
    }

    return render(request, "profiles/addresses.html", context)


@login_required()
def add_address(request):
    """
    View to render the 'add new address' form
    """
    if request.method == "POST":
        form = AddressForm(request.POST)
        if form.is_valid:
            address = form.save(commit=False)
            """
            checks that the user whose address is being edited
            is the same as the user who is currently logged in
            """
            address.user = request.user
            address.save()
            messages.success(request, "Address added successfully")
            return redirect("addresses")
    form = AddressForm()
    context = {"form": form}

    return render(request, "profiles/add-address.html", context)


@login_required()
def edit_address(request, address_id):
    """
    A view for editing existing saved addresses
    """
    address = get_object_or_404(
        ShippingAddress, id=address_id, user=request.user
    )
    if request.method == "POST":
        form = AddressForm(request.POST, instance=address)
        if form.is_valid():
            address = form.save(commit=False)
            """
            checks that the user whose address is being edited
            is the same as the user who is currently logged in
            """
            address.user = request.user
            address.save()
            messages.success(request, "Address edited successfully")
            return redirect("addresses")
    form = AddressForm(instance=address)
    context = {
        "form": form,
        "address": address,
    }
    return render(request, "profiles/edit-address.html", context)


@login_required()
def delete_address(request, address_id):
    """
    A view for deleting existing saved addresses
    """
    address = get_object_or_404(
        ShippingAddress, id=address_id, user=request.user
    )
    if request.method == "POST":
        address.delete()
        messages.success(request, "Address deleted successfully")
        return redirect("addresses")

    context = {
        "address": address,
    }

    return render(request, "profiles/delete-address.html", context)


@login_required()
def set_default_address(request):
    user = request.user
    new_default = int(request.POST["address_id"])

    for address in ShippingAddress.objects.filter(user=user):
        if address.id == new_default:
            address.default_address = True
        else:
            address.default_address = False
        address.save()

    return redirect("addresses")


@login_required()
def order_history(request):
    user = request.user
    orders = Order.objects.filter(user=request.user)

    context = {
        "user": user,
        "orders": orders,
    }

    return render(request, "profiles/order-history.html", context)
