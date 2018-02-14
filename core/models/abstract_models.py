from django.db import models


class BaseDjangoModel(models.Model):
    created = models.DateTimeField(verbose_name='Створено',auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(verbose_name='Оновлено',auto_now_add=False, auto_now=True)

    class Meta:

        abstract = True
