from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from product.models import Product
from product.models import Rice
from product.forms import RiceForm

class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'
    ordering = ['-id']

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'

def rice_create_view(request):
    if request.method == 'POST':
        form = RiceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success_url')
    else:
        form = RiceForm()   
    return render(request, 'rice.html', {'form': form})