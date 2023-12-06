from django import forms
from cloths.models import Cloth

class AddToCartForm(forms.Form):
    SIZE_CHOICES = (
                    ('S', 'S'),
                    ('M', 'M'),
                    ('L','L'),
                    ('XL', 'XL'),
                    ('XXL', 'XXL'))
    
    QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 26)]

    quantity = forms.TypedChoiceField(choices=QUANTITY_CHOICES, coerce=int)
    inplace = forms.BooleanField(required=False, widget=forms.HiddenInput)
    size = forms.TypedChoiceField(choices=SIZE_CHOICES)