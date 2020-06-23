from django.shortcuts import render
from django.conf import settings
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views  import APIView
from django.contrib.auth.models import User
from .serializer import UserSerializer

# Create your views here.
def index(request):

    return render(request, 'index.html')


class SettingsBackend(BaseBackend):

    def authenticate(self, request, username=None, password=None):
        login_valid = (settings.ADMIN_LOGIN == username)
        pwd_valid = check_password(password, settings.ADMIN_PASSWORD)
        if login_valid and pwd_valid:
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                # Create a new user. There's no need to set a password
                # because only the password from settings.py is checked.
                user = User(username=username)
                user.is_staff = True
                user.is_superuser = True
                user.save()
            return user
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

        
class UserList(APIView):
    def get(self, request, format=None):
        all_users = User.objects.all()
        # import pdb; pdb.set_trace()
        serializers = UserSerializer(all_users, many=True)
        return Response(serializers.data)