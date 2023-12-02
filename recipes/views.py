from django.shortcuts import render
from django.views.generic import (
    CreateView, ListView, DetailView, DeleteView, UpdateView
)

from django.contrib.auth.mixins import(
    UserPassesTestMixin, LoginRequiredMixin
)

from django.contrib.messages.views import SuccessMessageMixin

from .models import Recipe
from .forms import RecipeForm

# Create your views here.
class AddRecipe(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """
    Add recipe view
    """
    template_name = 'recipes/add_recipe.html'
    model = Recipe
    form_class = RecipeForm
    success_url = '/recipes'
    success_message = "Recipe added successfully!"

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


class EditRecipe(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    Edit a recipe
    """
    template_name = 'recipes/edit_recipe.html'
    model = Recipe
    form_class = RecipeForm
    success_url = '/recipes/'

    def test_func(self):
        return self.request.user == self.get_object().user


class DeleteRecipe(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    Deletes a recipe
    """
    model = Recipe
    success_url = '/recipes/'

    def test_func(self):
        return self.request.user == self.get_object().user