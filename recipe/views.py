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
from rest_framework import generics

from .models import Profile, Recipe, RecipeIngredient
from .serializer import (ProfileSerializer, RecipeSerializer,
                         RecipeIngredientSerializer, UserSerializer)
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

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

class ProfileList(generics.ListCreateAPIView):
    # permission_classes = (IsAuthenticated)
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
        

class Profiledetails(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (IsAuthenticated)  
    serializers = ProfileSerializer
    queryset = Profile.objects.all()


class IngredientList(generics.ListCreateAPIView):
    # permission_classes = (IsAuthenticated)
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


class Ingredientdetails(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (IsAuthenticated)  
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    lookup_field='name'

class CountryList(generics.ListCreateAPIView):
    # permission_classes = (IsAuthenticated)
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
       

class Countrydetails(generics.RetrieveDestroyAPIView): 
    #  # permission_classes = (IsAuthenticated)
    queryset = Country.objects.all()
    lookup_field='place'
    serializer_class = CountrySerializer
    
class RecipeIngredientList(generics.ListCreateAPIView):
    # permission_classes = (IsAuthenticated)
    queryset = RecipeIngredient.objects.all()
    serializer_class = RecipeIngredientSerializer
     

class RecipeIngredientdetails(generics.RetrieveUpdateDestroyAPIView):  
    # permission_classes = (IsAuthenticated)
    queryset = RecipeIngredient.objects.all()
    serializer_class = RecipeIngredientSerializer
    lookup_field = 'name'


class Recipes(generics.ListCreateAPIView):
    serializer_class = RecipeSerializer
    queryset = Recipe.objects.all()
    filter_backends=[filters.SearchFilter]
    search_fields = ['country','name','ingredients']

    def perform_create(self, serializer):
        serializer.save(user=Profile.objects.first())

class RecipeDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RecipeSerializer
    queryset = Recipe.objects.all()

class RecipesCountry(generics.ListAPIView):
    serializer_class = RecipeSerializer
    queryset = Recipe.objects.all()

    def get_queryset(self):
        country = self.kwargs['country']
        return Recipe.objects.filter(country=country)


class RecipesIngredients(generics.ListAPIView):
    serializer_class = RecipeSerializer
    queryset = Recipe.objects.all()

    def get_queryset(self):
        ingredients = self.kwargs['ingredients']
        return Recipe.objects.filter(ingredients__icontains=ingredients)
        


