from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    password = models.CharField(max_length=128)
    mobile = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.username} -- {self.email} -- {self.mobile}"
