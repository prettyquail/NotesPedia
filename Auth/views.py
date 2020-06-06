from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import  JSONParser
from django.http import HttpResponse, JsonResponse
from .serializer import documentSerializer, showDocumentSerializer, showNotificationSerializer
from .models import Document, Access, Notification
from unAuth.models  import User
# Create your views here.
@csrf_exempt
def showDocuments(request, id):
    print(id)
    if request.method == 'GET':
        document = Document.objects.all()
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
            user = User.objects.get(user_id=data['ownerId'])
            serializer.save()
            document = Document.objects.get(name=serializer.data['name'])
            notification = Notification(userId='P', notificationLabel=f"{user.name} added a new document {serializer.data['name']}", notificationBy=user,noificationType="Added", document_id=document)
            notification.save()
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
        user2 = User.objects.get(user_id=document.ownerId.user_id)
        access = Access(userId=user, documentId=document)
        notification = Notification(userId=userId, notificationLabel=f"{user2.name} given access {document.name}", notificationBy=user,noificationType="Given", document_id=document)
        notification.save()
        access.save()
        return JsonResponse({
                'response': '',
                'message': 'Access given Successfully',
                'status': 201
            }, status=201)


@csrf_exempt
def getNotifications(request, id):
    notification = Notification.objects.filter(userId="P") | Notification.objects.filter(userId=id)
    serializer = showNotificationSerializer(notification, many=True)
    return JsonResponse({
                'response': serializer.data,
                'message': 'Notification shown Successfully',
                'status': 200
            }, status=200)


# @csrf_exempt
# def checkDocumentAccess(request,user_id, documentId):
#     if request.method == 'GET':
#         access = Access(userId=user_id, documentId=documentId)
#         if len(access):
#         return JsonResponse({
#                 'response': True,
#                 'message': 'You have access to this document',
#                 'status': 200
#             }, status=200)
#         else: JsonResponse({
#                 'response': False,
#                 'message': 'You don\'t have access for this document',
#                 'status': 200
#             }, status=200)

