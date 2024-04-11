from django.contrib import admin
from django.urls import path

from products.views import products, index
#app_name='products'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('products/', products, name='products'),
    #path('', include('products.urls')),
    #path('', products, name='index')
]