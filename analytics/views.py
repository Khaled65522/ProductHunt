from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from products.models import Product
from .forms import ReviewForm

# Create your views here.
def analytics(request):
    return HttpResponse("Analytics will be displayed here")


@login_required
def add_review(request, id):
    try:
        product = Product.objects.get(id=id)
        
        # Prevent reviewing own product
        if product.owner == request.user:
            return redirect("detail_product", id=id)
            
        if request.method == 'POST':
            form = ReviewForm(request.POST)
            if form.is_valid():
                review = form.save(commit=False)
                review.product = product
                review.user = request.user
                review.save()
                
    except Product.DoesNotExist:
        pass
    
    return redirect("detail_product", id=id)
