from django.contrib import admin

from .models import Supplier, Product, ProductSupplierRelation


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'parent_supplier', 'debt_to_parent')
    search_fields = ['name']
    list_filter = ['city']  # Фильтрация по городу


    def clear_debt(self, request, queryset):
        """
        Очищает задолженность перед поставщиком у выбранных объектов.
        """
        updated_count = queryset.update(debt_to_parent=0)
        self.message_user(request, f'{updated_count} объектов успешно обновлены.')
    clear_debt.short_description = 'Очистить задолженность у выбранных поставщиков'

    actions = [clear_debt]

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'model', 'release_date')
    search_fields = ['name', 'model']
    ordering = ['release_date']

@admin.register(ProductSupplierRelation)
class ProductSupplierRelationAdmin(admin.ModelAdmin):
    list_display = ('id', 'supplier', 'product', 'added_on')
    autocomplete_fields = ['supplier', 'product']
