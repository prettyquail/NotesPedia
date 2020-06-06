from django.urls import path
from .views import showDocuments, createDocuments, grantAccess
urlpatterns = [
    path('show_documents/<int:id>', showDocuments),
    path('createDocument', createDocuments),
    path('grantAccess/user/<int:userId>/document/<int:documentId>', grantAccess)
]