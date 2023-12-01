from django.contrib import admin
from .models import Recipe

# Register your models here.
@admin.register(Recipe)

class RecipeAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'instructions',
        'ingredients',
        'image',
        'image_alt',
        'recipe_types',
        'cooking_method',
        'servings',
        'freezable'
    )
    list_filter = ('recipe_types', 'cooking_method',)
    prepopulated_fields = {'slug':('title',)}