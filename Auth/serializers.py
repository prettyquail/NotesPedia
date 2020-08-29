from rest_framework import serializers
from UnAuth.models import User
from .models import Document,Access,Notification

class DocumentSerializer(serializers.ModelSerializer):
	class Meta():
		model = Document
		fields = ( 'document_id','document_name', 'document_url','document_year','document_ownerid',
			'document_semester','document_access_type','document_year','create_date')

	def to_representation(self, instance):
		response = super().to_representation(instance)
		response['document_ownerid'] = userSerializer(instance.document_ownerid).data
		return response


class PrivateDocumentSerializer(serializers.ModelSerializer):

	class Meta():
		model = Document
		fields = ( 'document_id','document_name','document_year','document_ownerid',
			'document_semester','document_access_type','document_year','create_date')
	def to_representation(self, instance):
		response = super().to_representation(instance)
		response['document_ownerid'] = userSerializer(instance.document_ownerid).data
		return response

class grantAccessSerializer(serializers.ModelSerializer):
	class Meta():
		model = Access
		fields = ('__all__')

class userSerializer(serializers.ModelSerializer):
	class Meta():
		model = User
		fields = ('user_id', 'email', 'username',)

class NotificationSerializer(serializers.ModelSerializer):
	class Meta():
		model = Notification
		fields = ('__all__')