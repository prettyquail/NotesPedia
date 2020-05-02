from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import  JSONParser
from .models import User
from .serialzer import userSerializer
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


@csrf_exempt
def showUser(request):
    if request.method == 'GET':
        user = User.objects.all()
        serializer = userSerializer(user, many=True)
        return JsonResponse(serializer.data, safe = False, status=200)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = userSerializer(data= data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
