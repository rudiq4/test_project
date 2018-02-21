from django.conf.urls import url, include
from django.contrib import admin
from products import views


urlpatterns = [
    url(r'^product/(?P<product_id>\w+)/$', views.product, name='product'),
]
