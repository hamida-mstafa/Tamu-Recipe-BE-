from django.http import HttpResponse, Http404
from .models import Profile, Image, Country, Ingredient, RecipeIngredient
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .serializer import ProfileSerializer, ImageSerializer, CountrySerializer, IngredientSerializer, RecipeIngredientSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
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

class ImageList(APIView):
    def get(self, request, format=None):
        all_images = Image.objects.all()
        serializer = ImageSerializer(all_images, many=True)
        return Response(serializer.data) 

    def post(self, request, format=None):
        serializer = ImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST) 

class Imagedetails(APIView):  
    def getimage(self, name):
        try:
            return Image.objects.get(name=name)
        except Image.DoesNotExist:
            return Http404  

    def get(self, request, name, format=None):
        image = self.getimage(name)
        serializers = ImageSerializer(image)
        return Response(serializers.data)

    def put(self, request, name, format=None):
        image = self.getimage(name)
        serializers = ImageSerializer(image, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, name, format=None):
        image = self.getimage(name)
        image.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)          

class IngredientList(APIView):
    def get(self, request, format=None):
        all_ingredients = Ingredient.objects.all()
        serializer = IngredientSerializer(all_ingredients, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = IngredientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST) 

class Ingredientdetails(APIView):  
    def getingredient(self, name):
        try:
            return Ingredient.objects.get(name=name)
        except Ingredient.DoesNotExist:
            return Http404  

    def get(self, request, name, format=None):
        ingredient = self.getingredient(name)
        serializers = IngredientSerializer(ingredient)
        return Response(serializers.data)

    def put(self, request, name, format=None):
        ingredient = self.getingredient(name)
        serializers = IngredientSerializer(ingredient, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, name, format=None):
        ingredient = self.getingredient(name)
        ingredient.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)     

class CountryList(APIView):
    def get(self, request, format=None):
        all_countries = Country.objects.all()
        serializer = CountrySerializer(all_countries, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CountrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST) 

class Countrydetails(APIView):  
    def getcountry(self, place):
        try:
            return Country.objects.get(place=place)
        except Country.DoesNotExist:
            return Http404  

    def get(self, request, place, format=None):
        country = self.getcountry(place)
        serializers = CountrySerializer(country)
        return Response(serializers.data)

    def put(self, request, place, format=None):
        country = self.getcountry(place)
        serializers = CountrySerializer(country, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, place, format=None):
        country = self.getcountry(place)
        country.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)        

class RecipeIngredientList(APIView):
    # permission_classes = (IsAuthenticated)

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
    # permission_classes = (IsAuthenticated)

    def getrecipeingredient(self, name):
        try:
            return RecipeIngredient.objects.get(name=name)
        except RecipeIngredient.DoesNotExist:
            return Http404  

    def get(self, request, name, format=None):
        recipeingredient = self.getrecipeingredient(name)
        serializers = RecipeIngredientSerializer(recipeingredient)
        return Response(serializers.data)

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