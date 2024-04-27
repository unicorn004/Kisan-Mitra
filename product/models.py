
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_images/')
    category = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    weight = models.DecimalField(max_digits=6, decimal_places=2)
    sku = models.CharField(max_length=50)

    def __str__(self):
        return self.name
