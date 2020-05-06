from rest_framework import serializers
from .models import User

# class userSerializer(serializers.Serializer):
#     username = serializers.CharField(max_length=64)
#     email = serializers.EmailField(max_length=64)
#     password = serializers.CharField(max_length=128)
#     mobile = serializers.CharField(max_length=10)
#     createDate = serializers.DateField()

#     def createUser(self, validated_data):
#         return User.objects.create(validated_data)


class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'mobile', 'createDate', 'user_id']