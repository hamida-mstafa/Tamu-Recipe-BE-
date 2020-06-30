import json

from django.conf import settings
from django.contrib.auth.models import User
from django.core import serializers
from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Profile, Recipe, RecipeIngredient
from .serializer import (ProfileSerializer, RecipeSerializer,
                         RecipeIngredientSerializer, UserSerializer)

# Create your views here.
class UserList(APIView):
    def get(self, request, format=None):
        all_users = User.objects.all()
        serializers = UserSerializer(all_users, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = UserSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetails(APIView):
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

class ProfileList(APIView):
    def get(self, request, format=None):
        all_profiles = Profile.objects.all()
        serializer = ProfileSerializer(all_profiles, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST) 

class Profiledetails(APIView):  
    def getprofile(self, pk):
        try:
            return Profile.objects.get(pk=pk)
        except Profile.DoesNotExist:
            return Http404  

    def get(self, request, pk, format=None):
        profile = self.getprofile(pk)
        serializers = ProfileSerializer(profile)
        return Response(serializers.data)

    def put(self, request, pk, format=None):
        profile = self.getprofile(pk)
        serializers = ProfileSerializer(profile, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        profile = self.getprofile(pk)
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)              

class RecipeList(APIView):
    def get(self, request, format=None):
        all_recipes = Recipe.objects.all()
        serializer = RecipeSerializer(all_recipes, many=True)
        return Response(serializer.data) 

    def post(self, request, format=None):
        serializer = RecipeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST) 

class Recipedetails(APIView): 
    def getrecipe(self, name):
        try:
            return Recipe.objects.get(name=name)
        except Recipe.DoesNotExist:
            return Http404  

    def get(self, request, format=None):
        search_results=Recipe.objects.filter(name__icontains=self.request.query_params.get('name'))
        res=serializers.serialize('json',search_results)
        return Response(json.loads(res),status=status.HTTP_200_OK)

    def put(self, request, name, format=None):
        recipe = self.getrecipe(name)
        serializers = RecipeSerializer(recipe, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, name, format=None):
        recipe = self.getrecipe(name)
        recipe.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)                 

class RecipeIngredientList(APIView):
    def get(self, request, format=None):
        all_recipeingredients = RecipeIngredient.objects.all()
        serializer = RecipeIngredientSerializer(all_recipeingredients, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = RecipeIngredientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST) 

class RecipeIngredientdetails(APIView):  
    def getrecipeingredient(self, name):
        try:
            return RecipeIngredient.objects.get(name=name)
        except RecipeIngredient.DoesNotExist:
            return Http404  

    def get(self, request, format=None):
        search_results=RecipeIngredient.objects.filter(name__icontains=self.request.query_params.get('name'))
        res=serializers.serialize('json',search_results)
        return Response(json.loads(res),status=status.HTTP_200_OK)      

    def put(self, request, name, format=None):
        recipeingredient = self.getrecipeingredient(name)
        serializers = RecipeIngredientSerializer(recipeingredient, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, name, format=None):
        recipeingredient = self.getrecipeingredient(name)
        recipeingredient.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
