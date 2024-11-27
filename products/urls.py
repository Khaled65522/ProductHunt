from django.urls import path
from . import views

urlpatterns = [
    path("products/", views.all_products, name="all_products"),
    path('create-product/', views.create_product, name="create_product"),
]