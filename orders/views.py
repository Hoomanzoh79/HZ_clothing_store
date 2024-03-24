from django.shortcuts import render, redirect
from .forms import OrderForm
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
from .models import OrderItem, Order
from accounts.models import Profile


@login_required
def order_create_view(request):
    order_form = OrderForm()
    first_name = Profile.objects.get(user_id=request.user.id).first_name
    last_name = Profile.objects.get(user_id=request.user.id).last_name
    phone_number = Profile.objects.get(user_id=request.user.id).phone_number
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
                    price=cloth.price,
                )
            cart.clear()
            request.user.first_name = order_obj.first_name
            request.user.last_name = order_obj.last_name
            request.user.save()

            request.session['order_id'] = order_obj.id
            # return index just for testing this view
            return redirect('index')

    return render(request, 'orders/order_create.html', context={'form': order_form,
                                                                'first_name':first_name,
                                                                'last_name':last_name,
                                                                'phone_number':phone_number,})
