from django.db import models
from products.models import Product
from django.db.models.signals import post_save
from core.models.abstract_models import BaseDjangoModel


class Status(BaseDjangoModel):
    name = models.CharField(max_length=24, blank=True, null=True, default=None)  # blank-може бути пустим
    flag = models.BooleanField(default=True)

    def __str__(self):  # в адмінці
        return "Статус %s" % self.name

    class Meta:
        verbose_name = 'Статус замовлення'
        verbose_name_plural = 'Статуси замовлень'


class Order(BaseDjangoModel):
    total_price = models.DecimalField(verbose_name='Сумарна ціна',max_digits=10, decimal_places=2, default=0)
    customer_name = models.CharField(verbose_name='Імя покупця',max_length=64, blank=True, null=True, default=None)
    customer_email = models.EmailField(verbose_name='E-mail покупця',blank=True, null=True, default=None)
    customer_phone = models.CharField(verbose_name='Тел. номер покупця',max_length=48, blank=True, null=True, default=None)
    customer_address = models.CharField(verbose_name='Адрес покупця',max_length=128, blank=True, null=True, default=None)
    status = models.ForeignKey(Status)

    def __str__(self):
        return "Замовлення %s %s" % (self.id, self.status.name)

    class Meta:
        verbose_name = 'Замовлення'
        verbose_name_plural = 'Замовлення'

    def save(self, *args, **kwargs):
        super(Order, self).save(*args, **kwargs)


class ProductInOrder(BaseDjangoModel):
    order = models.ForeignKey(Order, blank=True, null=True, default=None)
    product = models.ForeignKey(Product, blank=True, null=True, default=None)
    nmb = models.IntegerField(default=1)  # Кількість товару
    price_per_item = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # Вартість одиниці товару
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # Повна вартість одного товару
    flag = models.BooleanField(default=True)

    def __str__(self):
        return "%s" % self.product.name

    class Meta:
        verbose_name = 'Товар в замовленні'
        verbose_name_plural = 'Товари у замовленні'

    def save(self, *args, **kwargs):  # Шаблон для перевизначення
        price_per_item = self.product.price  # З моделі products беремо вартість конкретної книги і зберіг
        self.price_per_item = price_per_item
        self.total_price = self.nmb * self.price_per_item  # к-сть*вартість книги
        super(ProductInOrder, self).save(*args, **kwargs)


def product_in_order_post_save(sender, instance, created, **kwargs):
    order = instance.order
    all_products_in_order = ProductInOrder.objects.filter(order=order, flag =True)
    order_total_price = 0
    for item in all_products_in_order:
        order_total_price += item.total_price
    instance.order.total_price = order_total_price
    instance.order.save(force_update=True)


post_save.connect(product_in_order_post_save, sender=ProductInOrder)
