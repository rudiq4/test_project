from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True, default=None)  # Назва книги
    autrhor = models.CharField(max_length=32, blank=True, null=True, default=None) # Автор книги
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0) # Ціна книги
    description = models.TextField(blank=True, null=True, default=None)  # Опис книги
    flag = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товари'


class ProductImage(models.Model):
    image = models.ImageField(upload_to='static/media/product_images/')  # Сюди зберігатимуться зобр. книжок
    product = models.ForeignKey(Product, blank=True, null=True, default=None)  # Посилання на саму книгу
    flag = models.BooleanField(default=True)  # Вкл/викл показ картинки товару
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.id

    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фотографії до товарів'


