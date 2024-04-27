from django.test import TestCase
from .models import Product, Category
from django.urls import reverse

class ProductTestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Test Category', description='Test Description')
        self.product = Product.objects.create(
            name='Test Product',
            description='Test Description',
            price=10.00,
            category=self.category,
            quantity=100,
            weight=1.5,
            sku='TEST123'
        )

    def test_product_creation(self):
        self.assertEqual(self.product.name, 'Test Product')
        self.assertEqual(self.product.description, 'Test Description')
        self.assertEqual(self.product.price, 10.00)
        self.assertEqual(self.product.category, self.category)
        self.assertEqual(self.product.quantity, 100)
        self.assertEqual(self.product.weight, 1.5)
        self.assertEqual(self.product.sku, 'TEST123')