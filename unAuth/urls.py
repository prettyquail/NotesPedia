from django.urls import path
from .views import showUser
urlpatterns = [
    path('register', showUser)
]
