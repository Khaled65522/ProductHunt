from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm

# Create your views here.
def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')

    else:
        form = ProductForm()
    return render(request, 'addproduct.html', {'form': form})

def detail_product(request, id):
    products = Product.objects.filter(id=id)  # Example filter
    return render(request, 'detail-product.html', {'products': products})


def update_product(request, id):
    p=Product.objects.get(id=id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=p)
        if form.is_valid():
                form.save()
                return redirect('/')

    else:
     form=ProductForm(instance=p)

     return render(request, 'addproduct.html', {'form': form})

def delete_product(request, id):
    Product.objects.get(id=id).delete()
    return redirect('/')



