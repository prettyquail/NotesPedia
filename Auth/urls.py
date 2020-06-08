from django.urls import path
from .views import showDocuments, createDocuments, grantAccess, getNotifications, myDocuments, wantAccess, checkDocumentAccess
urlpatterns = [
    path('show_documents/<int:id>', showDocuments),
    path('my_documents/<int:id>', myDocuments),
    path('createDocument', createDocuments),
    path('grantAccess/user/<int:userId>/document/<int:documentId>', grantAccess),
    path('get_notifications/<int:id>', getNotifications),
    path('wantAccess/user/<int:userId>/document/<int:documentId>', wantAccess),
    path('check_document_access/user/<int:userId>/document/<int:documentId>', checkDocumentAccess),
]