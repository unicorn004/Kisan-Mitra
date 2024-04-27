from django.db import models
import uuid

class ProductTable(models.Model):
    """
    Stores global configuration data of a company for the platform.
    """
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(verbose_name='Name', max_length=100, blank=False, unique=True)
    description = models.TextField(verbose_name='Description', blank=True)
    price = models.DecimalField(verbose_name='Price', max_digits=10, decimal_places=2)
    image = models.ImageField(verbose_name='Image', upload_to='product_images/')
    category = models.CharField(verbose_name='Category', max_length=100)
    quantity = models.PositiveIntegerField(verbose_name='Quantity')
    weight = models.DecimalField(verbose_name='Weight', max_digits=10, decimal_places=2)
    sku = models.CharField(verbose_name='SKU', max_length=100, unique=True)

    def __str__(self):
        return f"{self.program.name} ProductTable"
