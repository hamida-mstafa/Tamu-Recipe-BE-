from django.urls import path,re_path
from . import views as views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('api/profiles/' ,views.ProfileList.as_view()),
    path('api/images/', views.ImageList.as_view()),
    path('api/countries/' ,views.CountryList.as_view()),
    path('api/ingredients/', views.IngredientList.as_view()),
    path('api/recipeingredients/', views.RecipeIngredientList.as_view()),
    path('api/profile/profile_id/<pk>/', views.Profiledetails.as_view()),
    path('api/image/image_id/<name>/', views.Imagedetails.as_view()),
    path('api/country/country_id/<place>/', views.Countrydetails.as_view()),
    path('api/recipeingredient/recipeingredient_id/<name>/', views.RecipeIngredientdetails.as_view()),
    path('api/ingredient/ingredient_id/<name>/', views.Ingredientdetails.as_view()),
    
]

if settings.DEBUG:
  urlpatterns+= static(
    settings.MEDIA_URL, document_root = settings.MEDIA_ROOT
  )