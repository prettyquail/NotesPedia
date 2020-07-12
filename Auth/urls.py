from django.conf.urls import url
from django.urls import path
from .views import FileView
from . import views

urlpatterns = [
    url(r'^upload/', FileView.as_view(), name='file-upload'),
    path('document-list/', views.DocumentList, name="document-list"),
    path('document-update/<str:pk>/', views.DocumentUpdate, name="document-update"),
	path('document-delete/<str:pk>/', views.DocumentDelete, name="document-delete"),
	path('document-detail/<str:pk>/', views.MyDocuments, name="document-detail"),
	path('myprofile/<str:pk>/', views.MyProfile, name="profile"),
	path('profileupdate/<str:pk>/', views.ProfileUpdate, name="profileupdate"),
	path('checkaccess/<str:pk>/<str:docid>/', views.CheckAccess, name="check"),
	path('grantaccess/<str:pk>/<str:docid>/', views.GrantAccess, name="grant"),
	path('wantaccess/<str:pk>/<str:docid>/', views.wantAccess, name="want"),
	path('notifications/<str:pk>/', views.notifications, name="notifications"),
	path('rejectnotifications/<str:pk>/', views.Rejectnotifications, name="rejectnotifications"),
]
