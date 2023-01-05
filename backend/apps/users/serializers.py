from rest_framework import serializers
from .models import Users
from django.contrib.auth.hashers import make_password, check_password
from secrets import token_hex
import datetime

class signupserializer(serializers.ModelSerializer):
     profile = serializers.ImageField(read_only = True)
     email = serializers.CharField(required = True)
     password = serializers.CharField (write_only = True, required = True)
     token =  serializers.CharField(read_only = True)
     token_expires = serializers.DateTimeField(read_only = True)
     class Meta:
          model = Users
          fields = ('id', 'name', 'profile', 'email', 'password', 'token', 'token_expires')
     def create(self, validated_data):
          if Users.objects.filter(email = validated_data['email']).exists():
               raise serializers.ValidationError({'email':['this email already exists']})
          validated_data['password'] = make_password(validated_data['password'])
          validated_data['token'] = token_hex(30)
          validated_data['token_expires'] = datetime.datetime.now()+datetime.timedelta(days= 21)
          return super().create(validated_data)
         
class signinserializer(serializers.ModelSerializer):
     profile = serializers.ImageField(read_only = True)
     email = serializers.CharField(required = True)
     password = serializers.CharField (write_only = True, required = True)
     token =  serializers.CharField(read_only = True)
     token_expires = serializers.DateTimeField(read_only = True)
     class Meta:
          model = Users
          fields = ('id', 'name', 'profile', 'email', 'password', 'token', 'token_expires')
     def create(self, validated_data):
          user = Users.objects.filter(email = validated_data['email'])

          if len(user) >0 and check_password(validated_data['password'], user[0].password):
               
               user[0].token = token_hex(21)

               user[0].token_expires = datetime.datetime.now() + datetime.datetime(day=21)
               user[0].save()

               return user[0]
          else:
               raise serializers.ValidationError({"error": "Wrong email or password, try again."})