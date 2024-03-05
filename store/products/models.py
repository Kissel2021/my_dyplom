# Create your models here.

from django.db import models

class ProductCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

class Product(models.Model):
    name = models.CharField(max_length=255)
    image = models.CharField(max_length=255)
    description = models.TextField()
    short_description = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)

class User(models.Model):
    username = models.CharField(max_length=45)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.EmailField()
    password = models.CharField(max_length=45)
    image = models.CharField(max_length=255)

class Basket(models.Model):
    quantity = models.IntegerField()
    created = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)