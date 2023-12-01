from django.urls import path
from .views import AddRecipe, Recipes, FullRecipe

urlpatterns = [
    path('', AddRecipe.as_view(), name = 'add_recipe'),
    path('recipes', Recipes.as_view(), name='recipes'),
    path('recipes/<slug:pk>/', FullRecipe.as_view(), name='full_recipe'),
]