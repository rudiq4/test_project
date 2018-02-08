from django.contrib import admin
from .models import *


class ProductImageInline(admin.TabularInline):  # При добавлянні товару добавляєм йому картинку
    model = ProductImage
    extra = 1  # Тільки 1 поле для завантаження картинки


class ProductAdmin (admin.ModelAdmin):
    list_display = [field.name for field in Product._meta.fields]
    inlines = [ProductImageInline]  # Вкладення /картинки/

    class Meta:
        model = Product

admin.site.register(Product, ProductAdmin)


class ProductImageAdmin (admin.ModelAdmin):
    list_display = [field.name for field in ProductImage._meta.fields]

    class Meta:
        model = ProductImage

admin.site.register(ProductImage, ProductImageAdmin)