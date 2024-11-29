from django.urls import path
from . import views

urlpatterns = [
    path('create-product/', views.create_product, name="create_product"),
    path('detail-product/<int:id>', views.detail_product, name="detail_product"),
    path('update-product/<int:id>', views.update_product, name="update_product"),
    path('delete-product/<int:id>', views.delete_product, name="delete_product"),
]