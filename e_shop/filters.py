from django_filters.rest_framework import FilterSet

from e_shop.models import Supplier


class SupplierFilter(FilterSet):
    """Настраиваем фильтр по стране"""

    class Meta:
        model = Supplier
        fields = {"country": ["exact"]}
