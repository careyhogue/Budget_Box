from rest_framework import status
import datetime

from .models import Users
from config.helpers.error_response import error_response


class CustomLoginRequiredMixin():
     def dipatch(self, request, *args, **kwargs):
          if 'Autorization' not in request.headers:
               return error_response('please set auth-token', status.HTTP_401_UNAUTHORIZED)
          
          token = request.headers['Autorization']
          now = datetime.datetime.now()
          login_user = Users.objects.get(token =token, token_expires__gt = now )
          if len(login_user) == 0:
                return error_response('The token is invalid or expired', status.HTTP_401_UNAUTHORIZED)

          request.login_user = login_user[0]
          return super().dispatch(request, *args, **kwargs)