from django.db import models
from django.contrib.auth import get_user_model

class Team(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='team/', blank=True, null=True)
    designation = models.CharField(max_length=255)
    facebook = models.URLField(default='')
    twitter = models.URLField(default='')
    instagram = models.URLField(default='')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Category(models.Model):
    name = models.CharField(max_length=200)
    desc = models.CharField(max_length=1024)

    def __str__(self):
        return f'{self.name}'


class Product(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    product_image = models.ImageField(upload_to='products/', blank=True, null=True)
    price = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    categories = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='Catagory')

    def __str__(self):
        return f'{self.name} {self.categories}'
