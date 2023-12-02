from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Recipe
from .forms import RecipeForm

# Create your views here.
class AddRecipe(LoginRequiredMixin, CreateView):
    """
    Add recipe view
    """
    template_name = 'recipes/add_recipe.html'
    model = Recipe
    form_class = RecipeForm
    success_url = '/recipes'

    def form_valid(self, form):
        form.instance.user = self.request.user

        return super(AddRecipe, self).form_valid(form)



class Recipes(ListView):
    """
    View all recipes
    """
    template_name = 'recipes/recipes.html'
    model = Recipe
    context_object_name = 'recipes'


class FullRecipe(DetailView):
    """
    View full detail for single a recipe
    """
    template_name = 'recipes/full_recipe.html'
    model = Recipe
    context_object_name = 'recipe'