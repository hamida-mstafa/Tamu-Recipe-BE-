from django.test import TestCase
from .models import Profile, Ingredient, Country, Image
import datetime as dt
from django.contrib.auth.models import User
# Create your tests here.

class ProfileTestClass(TestCase):
    '''
    Test case for the Profile class and it's behaviours.
    '''
    #Set up method
    def setUp(self):
        self.new_user = User(username = "beryl", email = "beryl@gmail.com", password = "show001")
        self.new_user.save()
        self.new_profile = Profile(profile_pic = '/pic', bio = "hello world", contacts='beryl@gmail.com', user = self.new_user)
        self.new_profile.save()

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.new_profile, Profile))

    def tearDown(self):
        Profile.objects.all().delete()

    def test_save_method(self):
        profile = Profile.objects.all()
        self.assertTrue(len(profile) > 0)

    def test_update_method(self):
        profile = Profile.objects.all()
        self.assertTrue(len(profile) > 0)    

    def test_delete_method(self):
        profile = Profile.objects.all()
        self.new_profile.delete_profile()
        self.assertTrue(len(profile) == 0)

class ImageTestClass(TestCase):
    '''
    Test case for the Image class and it's behaviours.
    '''
    #Set up method
    def setUp(self):
        self.new_user = User(username = "beryl", email = "beryl@gmail.com", password = "show001")
        self.new_user.save()
        self.new_profile = Profile(profile_pic = '/posts', bio = "hello world", contacts = "beryl@gmail.com", user = self.new_user)
        self.new_profile.save()
        self.new_image = Image(name = 'chicken', ingredient = 'onions', country = 'Kenya', image = '/posts', recipe = 'hello new world', posted = '05/30/2020', profile = self.new_profile)
        self.new_image.save_image()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_image, Image))

    def tearDown(self):
        Image.objects.all().delete()

    def test_save_image(self):
        self.new_image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)

    def test_update_recipe(self):
        self.new_image.save_image()
        kwargs = {'image':'/posts', 'recipe':'hello new world'}
        Image.update_recipe(self.image.id, **kwargs)
        self.assertEqual("just a recipe", self.image.recipe)

    def test_delete_image(self):
        self.new_image.save_image()
        self.new_image.delete_image()
        images = Image.objects.all()
        self.assertTrue(len(images) == 0)        

class CountryTestClass(TestCase):
    '''
    Test case for the Country class and it's behaviours.
    '''
    # Set up method before any test case in this class
    def setUp(self):
        self.new_country = Country( locs = "Kenya")

    def tearDown(self):
        Country.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_country, Country))

    def test_save_method(self):
        self.new_country.save()
        countries = Country.objects.all()
        self.assertTrue(len(countries) > 0)

    def test_update_method(self):
        countries = Country.objects.all()
        self.assertTrue(len(countries) > 0)    

    def test_delete_method(self):
        countries = Country.objects.all()
        self.new_country.delete_country()
        self.assertTrue(len(countries) == 0)    

class IngredientTestClass(TestCase):
    '''
    Test case for the Ingredient class and it's behaviours.
    '''
    # Set up method
    def setUp(self):
        self.new_ingredient = Ingredient( ingredient = "Tomato")

    def tearDown(self):
        Ingredient.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_ingredient, Ingredient))

    def test_save_method(self):
        self.new_ingredient.save()
        ingredients = Ingredient.objects.all()
        self.assertTrue(len(ingredients) > 0)  

    def test_update_method(self):
        ingredients = Ingredient.objects.all()
        self.assertTrue(len(ingredients) > 0)    

    def test_delete_method(self):
        ingredients = Ingredient.objects.all()
        self.new_ingredent.delete_ingredient()
        self.assertTrue(len(ingredients) == 0)          