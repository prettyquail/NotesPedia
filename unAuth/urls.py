from django.urls import path
from .views import registerUser, login, sendOtp, forgotPassword
urlpatterns = [
    path('register', registerUser),
    path('login', login),
    path('send_otp', sendOtp),
    path('forgot_password', forgotPassword),
]
