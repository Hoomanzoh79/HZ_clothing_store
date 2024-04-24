from django.shortcuts import render, redirect
from .forms import OrderForm
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
from .models import OrderItem
from accounts.models import Profile


@login_required(redirect_field_name="")
def order_create_view(request):
    order_form = OrderForm()
    profile = Profile.objects.get(user_id=request.user.id)
    first_name = profile.first_name
    last_name = profile.last_name
    phone_number = profile.phone_number
    address = profile.address
    cart = Cart(request)
    if len(cart) == 0:
        return redirect('cart:cart_detail')

    if request.method == "POST":
        order_form = OrderForm(request.POST)
        if order_form.is_valid():
            order_obj = order_form.save(commit=False)
            order_obj.user = request.user
            order_obj.save()

            for item in cart:
                cloth = item['cloth_obj']
                OrderItem.objects.create(
                    order=order_obj,
                    cloth=cloth,
                    quantity=item['quantity'],
                    size=item['size'],
                    price=cloth.price,
                )
            cart.clear()
            request.user.first_name = order_obj.first_name
            request.user.last_name = order_obj.last_name
            request.user.save()

            request.session['order_id'] = order_obj.id
            return redirect('payment:payment_process')

    return render(request, 'orders/order_create.html', context={'form': order_form,
                                                                'first_name':first_name,
                                                                'last_name':last_name,
                                                                'phone_number':phone_number,
                                                                'address':address,
                                                                })
