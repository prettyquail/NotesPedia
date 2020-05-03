from django.urls import path
from .views import showUser, login
urlpatterns = [
    path('register', showUser),
    path('login', login)
]
