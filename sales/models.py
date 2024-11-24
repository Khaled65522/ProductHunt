from django.db import models


# Create your models here.
class Coupon(models.Model):
    code = models.CharField(max_length=255, unique=True, blank=False)
    expiry_date = models.DateField(blank=False)
    description = models.CharField(max_length=255, blank=False)
    discount = models.DecimalField(max_digits=5, decimal_places=2, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [models.Index(fields=['code'])]
        ordering = ['-created_at']

    def __str__(self):
        return self.code
