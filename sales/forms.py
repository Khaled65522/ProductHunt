from .models import Coupon
from django import forms


class CouponForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea(attrs={"rows": 4}))

    class Meta:
        model = Coupon
        fields = ["code", "description", "discount", "expiry_date"]

    def save(self, commit=True):
        coupon = super().save(commit=False)
        if commit:
            coupon.save()
        return coupon