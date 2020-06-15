from django.urls import path
from .views import Register,Login
from .import views

urlpatterns = [
    path('addUser/', Register.as_view(), name="register"),
   
    path('login/',Login.as_view(), name="login"),
      path('otp/<str:email>', views.sendOTP, name="otp"),
      path('forgotpass/',views.PasswordUpdate, name="forgotpass"),

   ]