from django import forms
from .models import Product
from .models import Rice

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

class RiceForm(forms.ModelForm):
    class Meta:
        model = Rice
        fields = ['type', 'image', 'description', 'market_value_price', 'discounted_price', 'quantity', 'weight', 'sku']
