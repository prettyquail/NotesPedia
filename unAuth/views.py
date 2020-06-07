from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import  JSONParser
from .models import User
from .serialzer import registerSerializer, showUserSerializer, userSerializer
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import EmailMultiAlternatives, send_mail


# Create your views here.
@csrf_exempt
def registerUser(request):
    # todo: to be removed when we are done with user login and register
    if request.method == 'GET':
#         user = User.objects.all()
          user = User.objects.values_list('name')
          print(user)
#         serializer = showUserSerializer(user, many=True)
#         return JsonResponse(serializer.data, safe = False, status=200)
          return user

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = registerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({
                'response': serializer.data,
                'message': 'User Registered Successfully',
                'status': 201
            }, status=201)
        return JsonResponse({
            "response": serializer.errors,
            "message": 'Registration failed',
            "status": 400
        }, status=400)

@csrf_exempt
def login(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        userdata = User.objects.filter(email=data['email'], password=data['password'])
        serializer = userSerializer(userdata, many=True)
        if len(serializer.data) > 0:
            return JsonResponse({
                            "response": serializer.data,
                            "message": 'Login success',
                            "status": 200
                        },safe = False, status=200)
        else:
            return JsonResponse({
                            "response": [],
                            "message": 'Invalid Email or Password',
                            "status": 404
                        },safe = False, status=404)
          

@csrf_exempt
def sendOtp(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        userdata = User.objects.filter(email=data['email'])
        serializer = userSerializer(userdata, many=True)
        if len(serializer.data) > 0:
            subject, from_email, to = 'Email Verification mail', 'gploswal@gmail.com', data['email']
            text_content = 'This mail is system generated'
            html_content = '<p>This is an <strong>important</strong> message.</p>'
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            send_mail('Subject here', 'Here is the message.', 'gploswal@gmail.com',
            ['viceversa2505@gmail.com'], fail_silently=False)
            print('msg')
            print(msg)
            return JsonResponse({
                            "response": '',
                            "message": 'OTP sent',
                            "status": 200
                        },safe = False, status=200)
        else:
            return JsonResponse({
                            "response": [],
                            "message": 'Email Doesnot Exist',
                            "status": 404
                        },safe = False, status=404)
        
@csrf_exempt
def forgotPassword(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        user = User.objects.get(email=data['email'])
        if user:
            user.password = data['new_password']
            user.save()
            return JsonResponse({
                                    "response": '',
                                    "message": 'Password reset successfull',
                                    "status": 200
                                },safe = False, status=200)
        else:
            return JsonResponse({
                                    "response": '',
                                    "message": 'Email Doesnot exist',
                                    "status": 404
                                },safe = False, status=404)
