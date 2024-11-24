from django.db import models
from accounts.models import User

# Create your models here.
class Product(models.Model):
    STATUS_CHOICES = [('pending', 'Pending'), ('accepted', 'Accepted'), ('rejected', 'Rejected')]
    name = models.CharField(max_length=255)
    icon = models.ImageField(upload_to='products/icons/')
    tagline = models.CharField(max_length=255)
    description = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products')
    tags = models.JSONField(default=list)
    website = models.URLField(max_length=200, blank=True, null=True)
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='pending',
    )
    featured = models.BooleanField(default=False)
    upvotes = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [models.Index(fields=['owner'])]
        ordering = ['-created_at']
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return f"{self.name} by {self.owner}"

class ProductUpvote(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='upvoted_by')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='upvoted_products')
    created_at = models.DateTimeField(auto_now_add=True)
