import django_filters
from django import forms
from django.forms.widgets import NumberInput
from django.utils.translation import gettext as _

from .models import Cloth,Category,Brand


class ClothFilter(django_filters.FilterSet):
    brand = django_filters.CharFilter(label=_('search brand'),
                                      widget=forms.TextInput(attrs={'placeholder': _('type the brand name')})
                                      )
    popular_brands = django_filters.ModelMultipleChoiceFilter(field_name='brand',
        label=_('popular brands'),                                           
        queryset=Brand.objects.all(),
        widget=forms.CheckboxSelectMultiple()
    )
    category = django_filters.ModelMultipleChoiceFilter(
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple()
    )
    gender = django_filters.MultipleChoiceFilter(
        choices=Cloth.GENDER_CHOICES,
        widget=forms.CheckboxSelectMultiple()
    )
    season = django_filters.MultipleChoiceFilter(
        choices=Cloth.SEASON_CHOICES,
        widget=forms.CheckboxSelectMultiple()
    )
    price__gt = django_filters.NumberFilter(field_name='price', lookup_expr 
    ='gte', label=_('min price'), widget=NumberInput(attrs={'placeholder': '0'}))
    price__lt = django_filters.NumberFilter(field_name='price', lookup_expr 
    = 'lte', label=_('max price'), widget=NumberInput(attrs={'placeholder': _('max price')}))

    class Meta:
        model = Cloth
        fields = []