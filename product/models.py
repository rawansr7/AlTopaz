from django.db import models
from user.models import User


class Product(models.Model):
    name = models.CharField(max_length=500)
    description = models.TextField()
    price = models.FloatField()
    stars = models.IntegerField()
    availability = models.IntegerField()
    image = models.ImageField()

    def __str__(self):
        return self.name


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)

    def __str__(self):
        return str(self.user)
