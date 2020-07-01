from rest_framework import serializers
from .models import Profile, Recipe, RecipeIngredient, Country
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')
        extra_kwargs = {
        'password': {'write_only': True, 'validators':[validate_password]},
        }

    def create(self, *args, **kwargs):
        return User.objects.create_user(*args, **kwargs)

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('user', 'bio', 'profile_pic','contacts')

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('place',)

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = '__all__'  
        
class RecipeIngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecipeIngredient
        fields = ('name',)           
        
                    
