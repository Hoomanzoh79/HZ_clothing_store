from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'phone_number', 'address','postal_code','order_notes', ]
        widgets = {
            'order_notes': forms.Textarea(attrs={
                'rows': 3, 'placeholder': 'If you have any notes please enter,'
                                          ' otherwise leave it empty'
            }),
            'address': forms.Textarea(attrs={'rows': 3}),
        }
