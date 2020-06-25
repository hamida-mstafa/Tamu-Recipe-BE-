from rest_framework import serializers
from .models import Profile, Image, Country, Ingredient, RecipeIngredient
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('user', 'bio', 'profile_pic','contacts')

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('name','recipe', 'ingredient', 'country', 'image', 'posted', 'profile')

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('place',)

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ('name','item','quantity', 'people_served')   

class RecipeIngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecipeIngredient
        fields = ('name',)           
        
                    
