from django import forms
from cloths.models import Cloth

class AddToCartForm(forms.ModelForm):
    
    QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 26)]

    quantity = forms.TypedChoiceField(choices=QUANTITY_CHOICES, coerce=int)
    inplace = forms.BooleanField(required=False, widget=forms.HiddenInput)

    class Meta:
        model = Cloth
        fields = ['sizes']
    
    
    def __init__(self, pk, *args, **kwargs):
            super(AddToCartForm, self).__init__(*args, **kwargs)
            sizes = tuple(Cloth.objects.get(pk=pk).sizes)
            sizes_list = []
            for item in sizes:
                sizes_list.append((item, item))
            self.fields['sizes'] = forms.ChoiceField(choices=sizes_list)
    