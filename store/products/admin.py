# Register your models here.
from django.contrib import admin
from .models import ProductCategory, Product, User, Basket

# Register your models here.


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'description', 'short_description', 'price', 'quantity', 'category')


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'password', 'image')


@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    list_display = ('quantity', 'created', 'user', 'product')

