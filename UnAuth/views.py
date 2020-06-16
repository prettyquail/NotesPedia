from django.shortcuts import redirect
from django.contrib.auth.base_user import BaseUserManager
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from .models import User
from .serializers import UserSerializer, UserLoginSerializer

from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from rest_framework.decorators import api_view
import random
from django.core.mail import send_mail
from django.conf import settings

class Register(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            data=serializer.data
            email = data.get('email')
            username = data.get('username')
            subject="Notespedia"
            html_message = render_to_string('UnAuth/register.html', {'username': username})
            plain_message = strip_tags(html_message)
            send_mail(
                subject,
                plain_message,
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=False,
            )


            return Response(serializer.data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    

class Login(generics.GenericAPIView):
    # get method handler
  
    queryset = User.objects.all()
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer_class = UserLoginSerializer(data=request.data)
       
        if serializer_class.is_valid(raise_exception=True):
            data=serializer_class.data
            email=data.get('email')
            token=data.get('token')
            user_id=data.get('user_id')
            msg={'email':email,'token':token,'user_id':user_id}

            return Response(msg, status=HTTP_200_OK)
        return Response(serializer_class.errors, status=HTTP_400_BAD_REQUEST)




"""@api_view(['GET'])
def sendOTP(request,pk):
    user=User.objects.get(user_id=pk)
    email=user.email
    subject='OTP'
    otp=random.randint(1111, 9999)
    html_message = render_to_string('UnAuth/otp.html', {'otp': otp})
    plain_message = strip_tags(html_message)
    rep_list=[email]
    send_mail(subject,plain_message,settings.EMAIL_HOST_USER,rep_list)
    return Response(otp, status=HTTP_200_OK)"""



"""@api_view(['POST'])
def sendOTP(request):
    serializer_class = UserSerializer(data=request.data)
    if serializer_class.is_valid(raise_exception=True):
        data=serializer_class.data
        user=data.get('email')
        if user:
            email=user
            subject='OTP'
            otp=random.randint(1111, 9999)
            html_message = render_to_string('UnAuth/otp.html', {'otp': otp})
            plain_message = strip_tags(html_message)
            rep_list=[email]
            send_mail(subject,plain_message,settings.EMAIL_HOST_USER,rep_list)
            return Response(otp, status=HTTP_200_OK)"""



@api_view(['GET'])
def sendOTP(request,email):
    user=User.objects.get(email=email)
    if user:
        email=user.email
        subject='OTP'
        otp=random.randint(1111, 9999)
        html_message = render_to_string('UnAuth/otp.html', {'otp': otp})
        plain_message = strip_tags(html_message)
        rep_list=[email]
        send_mail(subject,plain_message,settings.EMAIL_HOST_USER,rep_list)
        return Response(otp, status=HTTP_200_OK)






@api_view(['POST','PUT',])
def PasswordUpdate(request):
    data=request.data
    user = User.objects.get(email=data['email'])
    if user:
        user.password = data['newpassword']
        user.save()
        return Response("Sucessfully Updated",status=HTTP_200_OK)

