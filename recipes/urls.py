from django.urls import path
from .views import AddRecipe, Recipes, FullRecipe, DeleteRecipe, EditRecipe

urlpatterns = [
    path('', AddRecipe.as_view(), name = 'add_recipe'),
    path('recipes', Recipes.as_view(), name='recipes'),
    path('recipes/<slug:pk>/', FullRecipe.as_view(), name='full_recipe'),
    path('delete/<slug:pk>/', DeleteRecipe.as_view(), name='delete_recipe'),
    path('edit/<slug:pk>/', EditRecipe.as_view(), name='edit_recipe'),
]