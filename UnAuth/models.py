from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(models.Model):
	user_id=models.AutoField(primary_key=True)
	email=models.EmailField()
	username=models.CharField(max_length=55,blank=False)
	password=models.CharField(max_length=55,blank=False)
	phoneno = models.IntegerField(max_length=10,blank=True)
	about=models.CharField(max_length=20,blank=True)
	create_date=models.DateTimeField(auto_now_add=True)