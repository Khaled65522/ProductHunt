from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm

# Create your views here.
def my_products(request):
    products = Product.objects.filter(owner=request.user)
    return render(request, "myproducts.html", {"products": products})


def create_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        print(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.owner = request.user
            product.save()
            return redirect("home")
    else:
        form = ProductForm()
    return render(request, "product-form.html", {"form": form})


def detail_product(request, id):
    products = Product.objects.filter(id=id)  # Example filter
    return render(request, 'detail-product.html', {'products': products})


def update_product(request, id):
    p = Product.objects.get(id=id)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=p)
        if form.is_valid():
            form.save()
            return redirect("my_products")
    else:
        form = ProductForm(instance=p)
        # Convert tags list to comma-separated string
        if p.tags:
            form.initial["tags"] = ", ".join(p.tags)
        return render(request, "product-form.html", {"form": form})

def delete_product(request, id):
    Product.objects.get(id=id).delete()
    return redirect("my_products")



