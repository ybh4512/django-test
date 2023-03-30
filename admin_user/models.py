from django.db import models

# Create your models here.
class AdminUser(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)