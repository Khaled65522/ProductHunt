from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import  Coupon
from .forms import CouponForm

# Create your views here.
def my_coupons(request):
    coupons = Coupon.objects.filter(owner=request.user)
    return render(request, "sales/mycoupon.html", {"coupons": coupons})


def create_coupon(request):
    if request.method == "POST":
        form = CouponForm(request.POST, request.FILES)
        print(request.POST)
        if form.is_valid():
            coupon = form.save(commit=False)
            coupon.owner = request.user
            coupon.save()
            return redirect("home")
    else:
        form = CouponForm()
    return render(request, "sales/coupon-form.html", {"form": form})


def detail_coupon(request, id):
    try:
        coupon = Coupon.objects.get(id=id)
        return render(request, 'sales/detail-coupon.html', {'coupon': coupon})
    except Coupon.DoesNotExist:
        return redirect("my_coupons")
def update_coupon(request, id):
    p = Coupon.objects.get(id=id)
    if request.method == "POST":
        form = CouponForm(request.POST, request.FILES, instance=p)
        if form.is_valid():
            form.save()
            return redirect("my_coupons")
    else:
        form = CouponForm(instance=p)
        # Convert tags list to comma-separated string
        if p.tags:
            form.initial["tags"] = ", ".join(p.tags)
        return render(request, "coupon-form.html", {"form": form})


def delete_coupon(request, id):
    Coupon.objects.get(id=id).delete()
    return redirect("my_coupons")