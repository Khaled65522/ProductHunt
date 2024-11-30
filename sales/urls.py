from django.urls import path
from . import views

urlpatterns = [
    path("coupons/my/", views.my_coupons, name="my_coupons"),
    path("coupons/create/", views.create_coupon, name="create_coupon"),
    path("coupons/<int:id>/update/", views.detail_coupon, name="update_coupon"),
    path("coupons/<int:id>/detail/", views.detail_coupon, name="detail_coupon"),
    path("coupons/<int:id>/delete/", views.delete_coupon, name="delete_coupon")
]