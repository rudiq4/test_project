from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True, default=None)  # Назва товару
    description = models.TextField(blank=True, null=True, default=None)  # Опис товару
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товари'


class ProductImage(models.Model):
    image = models.ImageField(upload_to='static/media/product_images/')  # Сюди зберігатимуться пікчі товарів
    product = models.ForeignKey(Product, blank=True, null=True, default=None)  # Посилання на сам продукт
    flag = models.BooleanField(default=True)  # Вкл/викл показ картинки товару
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.id

    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фотографії'


