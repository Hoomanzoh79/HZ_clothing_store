from django.shortcuts import render
from .cart import Cart
from django.shortcuts import get_object_or_404,redirect
from cloths.models import Cloth
from .forms import AddToCartForm
from django.views.decorators.http import require_POST


def cart_detail_view(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = AddToCartForm(initial={
            'quantity': item['quantity'],
            'inplace': True,
        })
    return render(request, 'cart/cart_detail.html', {'cart': cart})


@require_POST
def add_to_cart_view(request, cloth_id):
    cart = Cart(request)
    cloth = get_object_or_404(Cloth, id=cloth_id)
    form = AddToCartForm(request.POST)
    if form.is_valid():
        cleaned_data = form.cleaned_data
        quantity = cleaned_data['quantity']
        cart.add(cloth, quantity, replace_current_quantity=cleaned_data['inplace'])

    return redirect('cart:cart_detail')


def remove_from_cart_view(request,cloth_id):
    cart = Cart(request)
    cloth = get_object_or_404(Cloth, id=cloth_id)
    cart.remove(cloth)
    return redirect('cart:cart_detail')