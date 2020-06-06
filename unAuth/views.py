from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import  JSONParser
from .models import User
from .serialzer import registerSerializer, showUserSerializer, userSerializer
from django.views.decorators.csrf import csrf_exempt

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

        

