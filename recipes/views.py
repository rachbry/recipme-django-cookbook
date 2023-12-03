from django.shortcuts import render
from django.views.generic import (
    CreateView, ListView, DetailView, DeleteView, UpdateView
)

from django.contrib.auth.mixins import(
    UserPassesTestMixin, LoginRequiredMixin
)

from django.db.models import Q
from django.core.exceptions import PermissionDenied
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

    def get_queryset(self, **kwargs):
        query = self.request.GET.get('q')
        if query:
            recipes = self.model.objects.filter(
                Q(title__icontains=query) |
                Q(description__icontains=query) |
                Q(instructions__icontains=query) |
                Q(ingredients__icontains=query) |
                Q(recipe_types__icontains=query) |
                Q(cooking_method__icontains=query) 
            )
        else:
            recipes = self.model.objects.all()
        return recipes


class MyRecipes(LoginRequiredMixin, ListView):
    """
    View personlised recipes for logged in user
    """
    template_name = 'recipes/my_recipes.html'
    model = Recipe
    context_object_name = 'recipes'

    def get_queryset(self, **kwargs):
        query = self.request.GET.get('q')
        user = self.request.user
        
        if query:
            recipes = self.model.objects.filter(
                Q(title__icontains=query) |
                Q(description__icontains=query) |
                Q(instructions__icontains=query) |
                Q(ingredients__icontains=query) |
                Q(recipe_types__icontains=query) |
                Q(cooking_method__icontains=query) 
            )
        else:
            recipes = self.model.objects.filter(user=user)
        return recipes


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
        return self.request.user.is_authenticated and self.request.user == self.get_object().user

    def handle_no_permission(self):
        # Raise a PermissionDenied exception
        raise PermissionDenied("You do not have permission to edit this recipe.")

    def handle_exception(self, exc):
        # Handle PermissionDenied exception and redirect to 403.html
        if isinstance(exc, PermissionDenied):
            messages.error(self.request, "You do not have permission to edit this recipe.")
            return render(self.request, '403.html', status=403)
        return HttpResponseForbidden()

    def form_valid(self, form):
        # If the form is valid, display a success message
        messages.success(self.request, 'Recipe updated successfully!')
        return super().form_valid(form)


class DeleteRecipe(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    Deletes a recipe
    """
    model = Recipe
    success_url = '/recipes/'

    def test_func(self):
        return self.request.user == self.get_object().user

    def handle_no_permission(self):
        # Raise a PermissionDenied exception
        raise PermissionDenied("You do not have permission to delete this recipe.")

    def handle_exception(self, exc):
        # Handle PermissionDenied exception and redirect to 403.html
        if isinstance(exc, PermissionDenied):
            messages.error(self.request, "You do not have permission to delete this recipe.")
            return render(self.request, '403.html', status=403)
        return HttpResponseForbidden()

    def form_valid(self, form):
        # If the form is valid, display a success message
        messages.success(self.request, 'Recipe deleted successfully!')
        return super().form_valid(form)