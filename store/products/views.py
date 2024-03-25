from django.shortcuts import render
from django.http import HttpResponse
from .models import ProductCategory, Product


def index(request):
    context = {
        'title': 'Store'
    }
    return render(request, 'products/index.html', context)


def products(request):
    context = {
        'title': 'Catalog',
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all(),
    }
    return render(request, 'products/products.html', context)#Переименовать в index.html
# Create your views here.

# def products(request):
#     context = {
#         'title': 'Store - Каталог'}
#         'products': Products.object.all(),
#         'categories': ProductCategory.object.all(),
#     }
#     return render(request, 'products/products.html', context)
#


def user(request):
    context = {
        'title': 'Страница авторизации'

    }
    return render(request, 'products/user.html', context)


def basket(request):
    context = {
        'title': 'Orders'
    }
    return render(request, 'products/user.html', context)