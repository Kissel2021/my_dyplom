from django.shortcuts import render
from .models import ProductCategory, Product, User, Basket


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
    return render(request, 'products/products.html', context)

# Create your views here.


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