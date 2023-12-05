from django.contrib.auth.models import User
from .models import Recipe

def is_favourite(user_id, recipe_id):
    user = User.objects.get(id=user_id)
    recipe = Recipe.objects.get(id=recipe_id)
    return recipe.favourites.filter(id=user.id).exists()