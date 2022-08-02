from django.shortcuts import render, get_object_or_404
from .models import Category, Product

# Create your views here.
'''
def home(request):
    return render(request,'tienda/index.html')


def category_list(request, category_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    return render(request, 'tienda/index.html', {'category': category, 'products': products})
    '''