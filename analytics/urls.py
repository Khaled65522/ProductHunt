from django.urls import path
from . import views

urlpatterns = [
    path("analytics/", views.analytics, name="analytics"),
    path("products/<int:id>/review/", views.add_review, name="add_review"),
]