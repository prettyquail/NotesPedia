from rest_framework import serializers
from .models import Document

class documentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ['name', 'url', 'year' ,'semester', 'accessType', 'ownerId']

class showDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ['document_id','name', 'url', 'year' ,'semester', 'accessType', 'ownerId', 'createDate']