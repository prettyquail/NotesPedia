from django.db import models
from UnAuth.models import User

class Document(models.Model):
	document_id = models.AutoField(primary_key=True)
	document_name = models.CharField(max_length=55,blank=False)
	document_url= models.CharField(max_length=55,blank=False)
	document_year = models.IntegerField(blank=False)
	document_semester = models.IntegerField(blank=False)
	document_access_type= models.CharField(max_length=20,blank=False)
	document_year = models.IntegerField(blank=False)
	document_ownerid = models.ForeignKey(User, on_delete=models.CASCADE)
	create_date = models.DateTimeField(auto_now_add=True,blank=False)



class Notification(models.Model):
	notification_id=models.AutoField(primary_key=True)
	notification_label=models.CharField(max_length=66)
	notification_by=models.ForeignKey(User,on_delete=models.CASCADE)
	user_id=models.IntegerField()
	document_id=models.ForeignKey(Document,on_delete=models.CASCADE)
	notification_type=models.CharField(max_length=55)


class Access(models.Model):
	access_id=models.AutoField(primary_key=True)
	user_id=models.ForeignKey(User,on_delete=models.CASCADE)
	document_id=models.ForeignKey(Document,on_delete=models.CASCADE)

