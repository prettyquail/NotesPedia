from django.db import models
from unAuth.models import User
# Create your models here.
class Document(models.Model):
    document_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=70, unique=True)
    url = models.CharField(max_length=512,unique=True)
    year = models.CharField(max_length=1)
    semester = models.CharField(max_length=1)
    accessType = models.CharField(max_length=1)
    ownerId = models.ForeignKey(User, on_delete=models.CASCADE)
    createDate = models.DateField(auto_now_add=True)

class Access(models.Model):
    accessId = models.AutoField(primary_key=True)
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    documentId = models.ForeignKey(Document, on_delete=models.CASCADE)