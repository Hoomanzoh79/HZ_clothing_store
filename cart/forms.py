from django import forms


class AddToCartForm(forms.Form):
    QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 26)]
    quantity = forms.TypedChoiceField(choices=QUANTITY_CHOICES, coerce=int)
