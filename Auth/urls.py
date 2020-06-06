from django.urls import path
from .views import showDocuments, createDocuments, grantAccess, getNotifications
urlpatterns = [
    path('show_documents/<int:id>', showDocuments),
    path('createDocument', createDocuments),
    path('grantAccess/user/<int:userId>/document/<int:documentId>', grantAccess),
    path('get_notifications/<int:id>', getNotifications)
]