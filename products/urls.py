from django.urls import path
from . import views

urlpatterns = [
    path("products/my/", views.my_products, name="my_products"),
    path("products/create/", views.create_product, name="create_product"),
    path("products/<int:id>/detail/", views.detail_product, name="detail_product"),
    path("products/<int:id>/update/", views.update_product, name="update_product"),
    path("products/<int:id>/delete/", views.delete_product, name="delete_product"),
]
