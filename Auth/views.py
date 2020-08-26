from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework import status
from .models import Document
from rest_framework.decorators import api_view
from .serializers import DocumentSerializer,PrivateDocumentSerializer,grantAccessSerializer,NotificationSerializer
from UnAuth.models import User
from .models import Access,Notification
from UnAuth.serializers import UserSerializer

class FileView(APIView):

  parser_classes = (MultiPartParser, FormParser)

  def post(self, request, *args, **kwargs):

    document_serializer = DocumentSerializer(data=request.data)
    if document_serializer.is_valid():
      document_serializer.save()
      return Response(document_serializer.data, status=status.HTTP_201_CREATED)
    else:
      return Response(document_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'DocumentList':'/document-list/',
		'Detail View':'/document-detail/<str:pk>/',
		'Update':'/task-update/<str:pk>/',
		'Delete':'/task-delete/<str:pk>/',
		}

	return Response(api_urls)


@api_view(['GET'])
def DocumentList(request):
	pubdocuments = Document.objects.filter(document_access_type='public')
	pridocuments = Document.objects.filter(document_access_type='private')
	serializer = DocumentSerializer(pubdocuments, many=True)
	priserializer = PrivateDocumentSerializer(pridocuments, many=True)
	msg={'public':serializer.data,'private':priserializer.data}
	return Response(msg,status=HTTP_200_OK)


	

@api_view(['GET'])
def MyDocuments(request, pk):
	documents = Document.objects.filter(document_ownerid=pk)
	serializer = DocumentSerializer(documents, many=True)
	return Response(serializer.data)


@api_view(['POST','PUT',])
def DocumentUpdate(request, pk):
	document = Document.objects.get(document_id=pk)
	serializer = DocumentSerializer(instance=document, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def DocumentDelete(request, pk):
	document = Document.objects.get(document_id=pk)
	document.delete()

	return Response('Item succsesfully delete!')

@api_view(['DELETE'])
def deleteNotification(request, id):
    notification = Notification.objects.get(notification_id=id)
    notification.delete()
    return Response("Deleted successfully")


@api_view(['GET'])
def MyProfile(request, pk):
	details = User.objects.get(user_id=pk)
	serializer = UserSerializer(details, many=False)
	return Response(serializer.data)


@api_view(['POST','PUT',])
def ProfileUpdate(request, pk):
	details = User.objects.gett(user_id=pk)
	serializer =UserSerializer(instance=details, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['GET'])
def CheckAccess(request,pk,docid):
	user_id= User.objects.get(user_id=pk)
	document_id=Document.objects.get(document_id=docid)
	exist=Access.objects.filter(user_id=user_id,document_id=document_id)
	msg={'exist':True,'document_url':document_id.document_url}
	if exist:
		return Response(msg,status=HTTP_200_OK)
	else:
		return Response("Sorry Access is not given", status=HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def GrantAccess(request,pk,docid):
	user_id= User.objects.get(user_id=pk)
	document_id=Document.objects.get(document_id=docid)
	access=Access.objects.create(user_id=user_id,document_id=document_id)
	serializer = grantAccessSerializer(instance=access,data=request.data)
	notification = Notification.objects.create(user_id=user_id.user_id, notification_label=f"{user_id.username} given access {document_id.document_name}", notification_by=user_id,notification_type="Given", document_id=document_id)
      
	if serializer.is_valid():
		serializer.save()
		return Response(serializer.data,status=HTTP_200_OK)
	else:
		return Response(" ", status=HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def wantAccess(request,pk,docid):
	user_id= User.objects.get(user_id=pk)
	document_id=Document.objects.get(document_id=docid)
	notificaton=Notification.objects.create(user_id=user_id.user_id, notification_label=f"{user_id.username} granted access for {document_id.document_name}", notification_by=user_id,notification_type="Asked", document_id=document_id)
	return Response("Sent Succsesfully",status=HTTP_200_OK)


@api_view(['GET'])
def notifications(request, pk):
	notifications = Notification.objects.filter(user_id=pk)
	serializer = NotificationSerializer(notifications, many=True)
	return Response(serializer.data)
