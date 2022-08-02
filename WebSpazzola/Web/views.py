from unicodedata import category
from django.shortcuts import render
from django.http import HttpResponse
from tienda.models import Category

# Create your views here.
def home(request):       
    categories = Category.objects.all()    
    return render(request,'tienda/index.html',{'categories':categories})



