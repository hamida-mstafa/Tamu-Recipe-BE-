from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
import datetime as dt

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    profile_pic = CloudinaryField('profile_pic')
    bio=models.CharField(max_length = 100)
    contacts=models.CharField(max_length = 100)

    def __str__(self):
        return self.bio

    @classmethod
    def save_profile(self):
        self.save()

    @classmethod
    def delete_profile(self):
        self.delete() 

    @classmethod
    def update_profile(self):
        self.update()    

class Country(models.Model):
    place = models.CharField(max_length=30)

    def __str__(self):
        return self.place

    @classmethod
    def save_country(self):
        self.save()
    
    @classmethod 
    def delete_country(self):
        self.delete()
        
    @classmethod
    def update_country(cls, id, new_country):
        cls.objects.filter(id=id).update(country=new_country)  

class RecipeIngredient(models.Model):
    name = models.CharField(max_length=70)

    def __str__(self):
        return self.name

    @classmethod
    def save_recipeingredient(self):
        self.save()
    
    @classmethod 
    def delete_recipeingredient(self):
        self.delete()    

class Ingredient(models.Model):
    name = models.CharField(max_length=70)
    item = models.ManyToManyField(RecipeIngredient)
    quantity = models.CharField(max_length=30)
    people_served = models.CharField(max_length=30)

    def __str__(self):
        return self.name
        
    @classmethod
    def save_ingredient(self):
        self.save()
    
    @classmethod 
    def delete_ingredient(self):
        self.delete()
        
    @classmethod
    def update_ingredient(cls, id, new_ingredient):
        cls.objects.filter(id=id).update(ingredient=new_ingredient)           

class Image(models.Model):
    name = models.CharField(max_length=60)
    recipe = models.TextField()
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    image = CloudinaryField('image')
    posted = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.name  

    @classmethod    
    def save_image(self):
        self.save()

    @classmethod
    def delete_image(self):
        self.delete()

    @classmethod
    def update_image(cls, id, value):
        cls.objects.filter(id=id).update(value)

    @classmethod
    def get_image_by_id(cls, id):
        return cls.objects.get(pk=id)

    @classmethod
    def search_by_category(cls,search_term):
        search_results = cls.objects.filter(category__name__icontains = search_term)
        return search_results

    @classmethod
    def search_by_country(cls, search_term):
        image = Image.objects.filter(country__id=search_term).all()
        return image

    @classmethod
    def search_by_ingredient(cls, search_term):
        image = Image.objects.filter(ingredient__id=search_term).all()
        return image       