from django.db import models
from products.models import Product


class Status(models.Model):
    name = models.CharField(max_length=24, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "Статус  %s" % self.name

    class Meta:
        verbose_name = 'Статус замовленяя'
        verbose_name_plural = 'Статуси замовленнь'

class Order(models.Model):# Поле Субскрайберс у ДБ де є 2 поля емейл і нейм.
    customer_email = models.EmailField(blank=True, null=True, default=None)
    customer_name = models.CharField(max_length=64, blank=True, null=True, default=None)
    customer_phone = models.CharField(max_length=48, blank=True, null=True, default=None)#blank - поле може бути empty
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now= True)
    comments = models.TextField(blank=True, null=True, default=None)
    status = models.ForeignKey(Status)

    def __str__(self):#В адмінці замість Subsriber object виводить людський вигляд
        return "Замовлення  %s %s" % (self.id, self.status.name)

    class Meta:
        verbose_name = 'Замовлення'
        verbose_name_plural = 'Замовлення'#В множині

class ProductinOrder(models.Model):
    order = models.ForeignKey(Order,blank=True, null=True, default=None)
    product = models.ForeignKey(Product,blank=True, null=True, default=None)
    is_active = models.ForeignKey(Status,)
    customer_email = models.EmailField(blank=True, null=True, default=None)
    customer_name = models.CharField(max_length=64, blank=True, null=True, default=None)
    customer_phone = models.CharField(max_length=48, blank=True, null=True, default=None)#blank - поле може бути empty
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now= True)

    def __str__(self):
        return "Товар  %s" % self.product.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товари'


