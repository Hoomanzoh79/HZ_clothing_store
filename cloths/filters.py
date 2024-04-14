import django_filters
from .models import Cloth

class ClothFilter(django_filters.FilterSet):

    brand = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Cloth
        fields = ['brand']