from django.urls import path
from .views import registerUser, login
urlpatterns = [
    path('register', registerUser),
    path('login', login)
]
