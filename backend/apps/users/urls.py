from django.contrib import admin
from django.urls import path, include
from .views import Signup
from .views import Signin


urlpatterns = [
    path('signin/', Signin.as_view()),
    path('signup/',Signup.as_view()), 
]