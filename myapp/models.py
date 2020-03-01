from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=32)

class Book(models.Model):
    title = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_rent = models.BooleanField(default=False)
