from django.db import models
from core.models.abstract_models import BaseDjangoModel


class BookType(BaseDjangoModel):
    name = models.CharField(verbose_name='Тип книги', max_length=32, blank=True, null=True, default=None)
    flag = models.BooleanField(verbose_name='Акт/Деакт', default=True)

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'Тип книги'
        verbose_name_plural = 'Типи книг'


class Product(BaseDjangoModel):
    name = models.CharField(verbose_name='Імя', max_length=64, blank=True, null=True, default=None)  # Назва книги
    book_type = models.ForeignKey(BookType, blank=True, null=True, default=None)
    autrhor = models.CharField(verbose_name='Автор', max_length=32, blank=True, null=True, default=None)  # Автор книги
    price = models.DecimalField(verbose_name='Ціна', max_digits=10, decimal_places=2, default=0)  # Ціна книги
    description = models.TextField(verbose_name='Опис', blank=True, null=True, default=None)  # Опис книги
    syte_description = models.TextField(verbose_name='Опис на сайті', blank=True, null=True, default=None) #  Опис книги на сайті
    flag = models.BooleanField(verbose_name='Акт/Деакт', default=True)

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товари'


class ProductImage(BaseDjangoModel):
    image = models.ImageField(upload_to='products_images/')  # Сюди зберігатимуться зобр. книжок
    product = models.ForeignKey(Product, blank=True, null=True, default=None)  # Посилання на саму книгу
    flag = models.BooleanField(default=True)  # Вкл/викл показ картинки товару
    main_picture = models.BooleanField(default=False)

    def __str__(self):
        return "%s" % self.id

    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фотографії до товарів'


