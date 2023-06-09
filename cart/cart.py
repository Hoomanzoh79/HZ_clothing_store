from cloths.models import Cloth


class Cart:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        cart = self.session.get('cart')

        if not cart:
            cart = self.session['cart'] = {}

        self.cart = cart

    def add(self, cloth, quantity=1, replace_current_quantity=False):
        cloth_id = str(cloth.id)

        if cloth_id not in self.cart:
            self.cart[cloth_id] = {'quantity': 0}

        if replace_current_quantity:
            self.cart[cloth_id]['quantity'] = quantity
        else:
            self.cart[cloth_id]['quantity'] += quantity

        self.save()

    def remove(self, cloth):
        cloth_id = str(cloth.id)
        if cloth_id in self.cart:
            del self.cart[cloth_id]
            self.save()

    def save(self):
        self.session.modified = True

    def __iter__(self):
        cloth_ids = self.cart.keys()
        cloths = Cloth.objects.filter(id__in=cloth_ids)
        cart = self.cart.copy()
        for cloth in cloths:
            cart[str(cloth.id)]['cloth_obj'] = cloth
        for item in self.cart.values():
            item['total_price'] = item['cloth_obj'].price * item['quantity']
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def clear(self):
        del self.session['cart']
        self.save()

    def get_total_price(self):
        return sum(item['cloth_obj'].price * item['quantity'] for item in self.cart.values())
