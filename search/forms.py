from django import forms
from cloths.models import Cloth


class ClothFilterForm(forms.ModelForm):
    class Meta:
        model = Cloth
        fields = ('category','season','gender','price',)
        