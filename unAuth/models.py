from django.db import models
from rest_framework import serializers
# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=64)
    email = models.EmailField(max_length=64)
    password = models.CharField(max_length=128)
    mobile = models.CharField(max_length=10)
    createDate = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.username} -- {self.email} -- {self.mobile}"

