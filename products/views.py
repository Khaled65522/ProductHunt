from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def all_products(request):
    return HttpResponse("All Products will be displayed here.")