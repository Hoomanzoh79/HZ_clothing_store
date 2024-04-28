from django.shortcuts import render
from .cart import Cart
from django.shortcuts import get_object_or_404,redirect
from cloths.models import Cloth
from .forms import AddToCartForm
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.utils.translation import gettext as _


def cart_detail_view(request):
    cart = Cart(request)

    return render(request, 'cart/cart_detail.html', {'cart': cart})


@require_POST
def add_to_cart_view(request, cloth_id):
    cart = Cart(request)
    cloth = get_object_or_404(Cloth, id=cloth_id)
    pk = cloth.pk
    form = AddToCartForm(data=request.POST,instance=cloth,pk=pk)
    
    if form.is_valid():
        cleaned_data = form.cleaned_data
        quantity = cleaned_data['quantity']
        size = cleaned_data['sizes']
        cart.add(cloth, size ,quantity, replace_current_quantity=cleaned_data['inplace'])
        messages.success(request, _('Product has been added successfully to the cart'))
        return redirect('cart:cart_detail')

    return redirect(cloth.get_absolute_url())


def remove_from_cart_view(request,cloth_id):
    cart = Cart(request)
    cloth = get_object_or_404(Cloth, id=cloth_id)
    cart.remove(cloth)
    messages.success(request, _('Product has been removed successfully from the cart'))
    return redirect('cart:cart_detail')


def clear_cart(request):
    cart = Cart(request)
    if len(cart):
        cart.clear()
        messages.success(request, _('Your cart has been successfully cleared '))
    else:
        messages.warning(request, _('Your cart is already empty'))
    return redirect('index')