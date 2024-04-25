import django_filters
from django import forms


from .models import Cloth

class ClothFilter(django_filters.FilterSet):
    price = django_filters.RangeFilter()
    category = django_filters.MultipleChoiceFilter(
        choices=Cloth.CATEGORIES,
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

    class Meta:
        model = Cloth
        fields = ["brand"]