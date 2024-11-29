from django.db import models
from accounts.models import User
from products.models import Product

# Create your models here.
class Report(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reports')
    reported_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Report'
        verbose_name_plural = 'Reports'
        indexes = [models.Index(fields=['product', 'reported_by'])]
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.product.name} reported by {self.reported_by.first_name}"


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(1,1), (2,2), (3,3), (4,4), (5,5)])
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [models.Index(fields=['product'])]
