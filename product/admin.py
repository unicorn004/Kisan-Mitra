from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category', 'quantity']
    search_fields = ['name', 'category__name']
    list_filter = ['category']
    list_editable = ['price', 'quantity']
