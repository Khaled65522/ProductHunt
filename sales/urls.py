from django.urls import path
from . import views

urlpatterns = [
    path("sales/", views.all_sales, name="all_sales"),
]