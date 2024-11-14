from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    image = models.ImageField(upload_to='profile_pics')
    role = models.CharField(
        max_length=10,
        choices=[("admin", "Admin"), ("moderator", "Moderator"), ("member", "Member")],
        default="member")
    is_subscribed = models.BooleanField(default=False)
    products_launched = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.user.username

