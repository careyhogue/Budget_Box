from django.db import models
from cloudinary.models import CloudinaryField


class Users(models.Model):
     class Meta(object):
          db_table = 'user'

     name = models.CharField(
          'Name', blank=False, null=False, max_length=150
     )
     email = models.EmailField(
          'Email', blank=False, null=False, max_length=150, unique=True
     )
     password = models.CharField(
          'password', blank=False, null=False, max_length=50
     )
     budget = models.IntegerField(
        'Budget', blank=False, null=False, default=0
     )
     token = models.CharField(
        'Token', blank=True, null=True, max_length=500, db_index=True
     )
     profile = CloudinaryField(
        "Profile Picture", blank=True, null=True
     )
     token_expires = models.DateTimeField(
        'Token Expiration Date', blank=True, null=True
     )
     created_at = models.DateTimeField(
        'Creation Date', blank=True, auto_now_add=True
     )
     updated_at = models.DateTimeField(
        'Update Date', blank=True, auto_now=True
     )
     def __str__(self):
        return self.name 