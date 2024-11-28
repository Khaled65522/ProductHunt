from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import  *
from .forms import *

# Create your views here.
def all_products(request):
    #return HttpResponse("All Products will be displayed here.")
    #request.method = "GET"
    products = Product.objects.all()
    return render(request, 'product.html', {'products': products})

def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')

    else:
        form = ProductForm()
    return render(request, 'addproduct.html', {'form': form})

def update_product(request, p_id):
    p=Product.objects.get(id=p_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=p)
        if form.is_valid():
                form.save()
                return redirect('/')

    else:
     form=ProductForm(instance=p)

     return render(request, 'addproduct.html', {'form': form})


