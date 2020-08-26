  
from django.db.models import Q # for queries
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User
from django.core.exceptions import ValidationError
from uuid import uuid4


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
        )
    username = serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
        )
    password = serializers.CharField(max_length=55)
    phoneno = serializers.IntegerField(required=False)
    about = serializers.CharField(required=False)

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password',
            'about',
            'phoneno'
        )

    

class UserLoginSerializer(serializers.ModelSerializer):
    
    email = serializers.EmailField()
    password = serializers.CharField()
    token = serializers.CharField(required=False, read_only=True)

    def validate(self, data):
        # user,email,password validator
        email = data.get("email", None)
        password = data.get("password", None)
        if not email and not password:
            raise ValidationError("Details not entered.")
        user = None
        # if the email has been passed
        if '@' in email:
            user = User.objects.filter(
                Q(email=email) &
                Q(password=password)
                ).distinct()
            if not user.exists():
                raise ValidationError("User credentials are not correct.")
            user = User.objects.get(email=email)
        
      
        data['token'] = uuid4()
        user.token = data['token']
        user.save()
    
        return user


    class Meta:
        model = User
        fields = (
            'email',
            'password',
            'token',
            'user_id',
        )

        read_only_fields = (
            'token',
        )
