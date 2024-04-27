from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    category = models.TextField()
    quantity = models.IntegerField(default=0)
    weight = models.DecimalField(max_digits=10, decimal_places=2)
    sku = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Rice(models.Model):
    TYPE_CHOICES = [
        ('Basmati', 'Basmati'),
        ('Jasmine', 'Jasmine'),
        ('Brown', 'Brown'),
        ('White', 'White'),
        ('Wild', 'Wild'),
        ('Arborio', 'Arborio'),
        ('Short Grain', 'Short Grain'),
        ('Long Grain', 'Long Grain'),
        ('Medium Grain', 'Medium Grain'),
        ('Red Rice', 'Red Rice'),
        ('Black Rice', 'Black Rice'),
        ('Parboiled', 'Parboiled'),
        ('Other', 'Other'),
    ]

    name = models.CharField(max_length=255)
    description = models.TextField()
    market_value_price = models.DecimalField(max_digits=10, decimal_places=2)
    discounted_price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='rice/', blank=True, null=True)
    type = models.CharField(max_length=50, choices=TYPE_CHOICES)
    quantity = models.IntegerField(default=0)
    weight = models.DecimalField(max_digits=10, decimal_places=2)
    sku = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name