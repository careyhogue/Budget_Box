from django.shortcuts import render
from rest_framework import generics
from .models import Users
from .serializers import signupserializer
from .serializers import signinserializer


class Signup(generics.CreateAPIView):
     queryset = Users.objects.all()
     serializer_class = signupserializer

class Signin(generics.CreateAPIView):
     queryset = Users.objects.all()
     serializers_class = signinserializer
