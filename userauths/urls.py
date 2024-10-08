from django.urls import path
from .views import register, userlogin, userlogout

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', userlogin, name='login'),
    path('logout/', userlogout, name='logout'),
]