from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название товара")
    model = models.CharField(max_length=255, verbose_name="Модель")
    release_date = models.DateField(verbose_name="Дата выхода продукта на рынок")

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return self.name


class Supplier(models.Model):

    name = models.CharField(max_length=255, verbose_name="Наименование поставщика")
    email = models.EmailField(verbose_name="Email")
    country = models.CharField(max_length=255, verbose_name="Страна")
    city = models.CharField(max_length=255, verbose_name="Город")
    street = models.CharField(max_length=255, verbose_name="Улица")
    house_number = models.CharField(max_length=10, verbose_name="Номер дома")

    # Поле определяет родителя, задаёт связь по одному родителю
    parent_supplier = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='children')

    # Связь продуктов с поставщиками
    products = models.ManyToManyField(Product, through='ProductSupplierRelation')

    # Задолженность перед родительским объектом
    debt_to_parent = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Поставщик"
        verbose_name_plural = "Поставщики"

    def __str__(self):
        return self.name


# Промежуточная таблица для связи поставщиков и товаров
class ProductSupplierRelation(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, verbose_name="Поставщик")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Товар")
    added_on = models.DateTimeField(auto_now_add=True, verbose_name="Дата добавления")

    class Meta:
        verbose_name = "Отношение Товар-Поставщик"
        verbose_name_plural = "Отношения Товары-Поставщики"