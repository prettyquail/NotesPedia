from rest_framework import serializers
from .models import Document, Notification

class documentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ['name', 'url', 'year' ,'semester', 'accessType', 'ownerId']

class showDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ['document_id','name', 'url', 'year' ,'semester', 'accessType', 'ownerId', 'createDate']

class showPrivateDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ['document_id','name', 'year' ,'semester', 'accessType', 'ownerId', 'createDate']

class showNotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['notification_id', 'userId','notificationLabel','notificationBy','noificationType','document_id','createDate']