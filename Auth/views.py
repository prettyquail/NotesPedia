from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import  JSONParser
from django.http import HttpResponse, JsonResponse
from .serializer import documentSerializer, showDocumentSerializer
from .models import Document, Access
from unAuth.models  import User
# Create your views here.
@csrf_exempt
def showDocuments(request, id):
    print(id)
    if request.method == 'GET':
        document = Document.objects.filter(accessType='S')
        serializer = showDocumentSerializer(document, many=True)
        return JsonResponse({
                'response': serializer.data,
                'message': 'Documents got successfully',
                'status': 200
            }, status=200)

@csrf_exempt
def createDocuments(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = documentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({
                'response': '',
                'message': 'Document created Successfully',
                'status': 201
            }, status=201)
        else: 
            return JsonResponse({
                'response': serializer.errors,
                'message': 'Document addition failed',
                'status': 400
            }, status=400)

@csrf_exempt
def grantAccess(request, userId , documentId):
    if request.method == 'GET':
        user = User.objects.get(user_id=userId)
        document = Document.objects.get(document_id=documentId)
        access = Access(userId=user, documentId=document)
        access.save()
        return JsonResponse({
                'response': '',
                'message': 'Access given Successfully',
                'status': 201
            }, status=201)