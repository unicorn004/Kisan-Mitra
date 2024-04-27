from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'image', 'category', 'quantity', 'weight', 'sku']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }

class ProductUpdateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'image', 'category', 'quantity', 'weight', 'sku']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }
