from django.db import models
from datetime import datetime, timedelta
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.


class Coupon(models.Model):
    code = models.CharField(max_length=255, unique=True, blank=False)
    expiry_date = models.DateField(default=datetime.now() + timedelta(days=30))
    description = models.CharField(max_length=255, blank=False)
    discount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [models.Index(fields=['code'])]
        ordering = ['-created_at']

    def __str__(self):
        return self.code
