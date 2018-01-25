from django.contrib import admin
from .models import *#С текущей папки импортировать все модели,которые находятся в файле models

#Тут реєструємо які моделі можна буде редагувати в адмінці

# class SubscriberAdmin(admin.ModelAdmin):
#     list_display = [field.name for field in Subscriber._meta.fields]#Красивіше оформлення ,вивід кожного окремо + ІД
#     search_fields = ["name","email"]# Пошук юзера по імені і емейлу
#
#     #exclude = ["email"]# Не показувати поле
#     #fields = ["name"]# Показувати поле
#     #list_filter =  #Сортування юзерів
#
#
#     class Meta:
#         model = Subscriber
#
#
# admin.site.register(Subscriber, SubscriberAdmin)






