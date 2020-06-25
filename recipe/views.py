from django.shortcuts import render
from django.conf import settings
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views  import APIView
from django.contrib.auth.models import User
from .serializer import UserSerializer
from rest_framework import status

# Create your views here.

        
class UserList(APIView):
    def get(self, request, format=None):
        all_users = User.objects.all()
        # import pdb; pdb.set_trace()
        serializers = UserSerializer(all_users, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = UserSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    
class UserDetails(APIView):
    # permission_classes = (IsAdminOrReadOnly,)
    def get_user(self, username):
        try:
            return User.objects.get(username=username)
        except User.DoesNotExist:
            return Http404

    def get(self, request, username, format=None):
        user = self.get_user(username)
        serializers = UserSerializer(user)
        return Response(serializers.data)

    def put(self, request, username, format=None):
        user = self.get_user(username)
        serializers = UserSerializer(user, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, username, format=None):
        user = self.get_user(username)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)