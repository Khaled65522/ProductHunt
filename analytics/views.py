from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def analytics(request):
    return HttpResponse("Analytics will be displayed here")