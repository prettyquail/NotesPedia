from rest_framework import serializers

from .models import Document,Access

class DocumentSerializer(serializers.ModelSerializer):

  class Meta():
    model = Document
    fields = ( 'document_id','document_name', 'document_url','document_year','document_ownerid',
    	'document_semester','document_access_type','document_year','create_date')


class PrivateDocumentSerializer(serializers.ModelSerializer):

  class Meta():
    model = Document
    fields = ( 'document_id','document_name','document_year','document_ownerid',
    	'document_semester','document_access_type','document_year','create_date')

class grantAccessSerializer(serializers.ModelSerializer):
	class Meta():
		model = Access
		fields = ('__all__')