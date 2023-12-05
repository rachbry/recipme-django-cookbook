def add_fav_to_context(request):
    def is_favourite(user, recipe_id):
        recipe = Recipe.objects.get(id=recipe_id)
        return recipe.favourites.filter(id=user.id).exists()

    return {'is_favourite': is_favourite}