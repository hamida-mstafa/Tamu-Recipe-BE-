from django.contrib import admin
from .models import Profile, Image, Country, Ingredient, RecipeIngredient

# Register your models here.
admin.site.register(Profile)
admin.site.register(Image)
admin.site.register(Country)
admin.site.register(Ingredient)
admin.site.register(RecipeIngredient)
