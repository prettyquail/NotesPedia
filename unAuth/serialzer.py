from rest_framework import serializers
from .models import User

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'email', 'password', 'mobile', 'createDate', 'user_id']


class registerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'email', 'password', 'createDate', 'user_id']

class showUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name']
