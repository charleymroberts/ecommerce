from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import AddressForm
from .models import ShippingAddress

@login_required()
def my_account(request):
    '''
    View to render the 'My Account' landing page
    '''

    return render(request, 'profiles/account.html')


@login_required()
def addresses(request):
    '''
    View to render the add/edit shipping addresses page
    '''
    user_addresses = ShippingAddress.objects.filter(user=request.user)

    context = {
        'user_addresses': user_addresses,
    }

    return render(request, 'profiles/addresses.html', context)


def add_address(request):
    '''
    View to render the 'add new address' form
    '''
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid:
            address = form.save(commit=False)
            address.user = request.user # checks that the person whose address is being edited is actually the user who is currently logged in
            address.save()
            messages.success(request, "Address added successfully")
            return redirect('addresses')
    form = AddressForm()
    context = {
        'form': form
    }

    return render(request, 'profiles/add-address.html', context)