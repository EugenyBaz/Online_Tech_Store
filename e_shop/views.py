from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet

from e_shop.filters import SupplierFilter
from e_shop.models import Supplier
from e_shop.permissions import ActiveEmployeeOnly
from e_shop.serializers import SupplierSerializer


class SupplierViewSet(ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    permission_classes = [ActiveEmployeeOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_class = SupplierFilter

    # Запрещаем обновление поля "debt_to_parent" через API
    def perform_update(self, serializer):
        instance = serializer.instance
        original_debt = instance.debt_to_parent
        updated_instance = serializer.save()

        # Если кто-то пытался поменять долг через API, восстанавливаем старое значение
        if original_debt != updated_instance.debt_to_parent:
            updated_instance.debt_to_parent = original_debt
            updated_instance.save(update_fields=["debt_to_parent"])
