from django.urls import path,re_path
from . import views as views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('api/user/', views.UserList.as_view()),
    path('api/profiles/' ,views.ProfileList.as_view()),
    #path('api/recipes/', views.RecipeList.as_view()),
    path('api/ingredients/', views.IngredientList.as_view()),
    path('api/recipeingredients/', views.RecipeIngredientList.as_view()),

    path('api/user/user-id/<username>/',views.UserDetails.as_view()),
    path('api/profile/profile_id/<pk>/', views.Profiledetails.as_view()),
    #path('api/recipe/recipe_id/', views.Recipedetails.as_view()),
    path('api/recipeingredient/recipeingredient_id/', views.RecipeIngredientdetails.as_view()),
    path('api/ingredient/ingredient_id/', views.Ingredientdetails.as_view()),

    path('api/recipes/', views.Recipes.as_view()),
    path('api/recipes/name/<name>/', views.Recipes.as_view()),
    path('api/recipes/country/<country>/', views.RecipesCountry.as_view()),
    path('api/recipes/ingredients/<ingredients>/', views.RecipesIngredients.as_view()),
    path('api/recipes/<pk>/', views.RecipeDetail.as_view()),
    
]

if settings.DEBUG:
  urlpatterns+= static(
    settings.MEDIA_URL, document_root = settings.MEDIA_ROOT
  )
