from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    CreateView, ListView, DetailView, DeleteView, UpdateView
)
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import(
    UserPassesTestMixin, LoginRequiredMixin
)

from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.db.models import Q
from django.core.exceptions import PermissionDenied
from django.contrib.messages.views import SuccessMessageMixin

# from utils.helpers import get_queryset_with_query
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
    View personalized recipes for the logged-in user
    """
    template_name = 'recipes/my_recipes.html'
    model = Recipe
    context_object_name = 'recipes'

    def get_queryset(self):
        query = self.request.GET.get('q')
        user = self.request.user

        base_query = (
            Q(title__icontains=query) |
            Q(description__icontains=query) |
            Q(instructions__icontains=query) |
            Q(ingredients__icontains=query) |
            Q(recipe_types__icontains=query) |
            Q(cooking_method__icontains=query)
        )

        recipes = self.model.objects.all()

        if query:
            recipes = recipes.filter(base_query)

        filtered_recipes = recipes.filter(Q(user=user) | Q(user__is_staff=True))

        return filtered_recipes


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


class SearchResultsView(ListView):
    template_name = 'recipes/search_results.html'
    model = Recipe
    context_object_name = 'recipes'

    def get_queryset(self):
        query = self.request.GET.get('q')
        user = self.request.user

        if query and user.is_authenticated:
            # Customize the queryset for authenticated users
            recipes = Recipe.objects.filter(
                Q(title__icontains=query) |
                Q(description__icontains=query) |
                Q(instructions__icontains=query) |
                Q(ingredients__icontains=query) |
                Q(recipe_types__icontains=query) |
                Q(cooking_method__icontains=query),
                Q(user=user) | Q(user__is_staff=True)
            )
        elif query:
            # For non-authenticated users, show general results
            recipes = Recipe.objects.filter(
                Q(title__icontains=query) |
                Q(description__icontains=query) |
                Q(instructions__icontains=query) |
                Q(ingredients__icontains=query) |
                Q(recipe_types__icontains=query) |
                Q(cooking_method__icontains=query)
            )
        else:
            # No query, show all recipes
            recipes = Recipe.objects.all()

        return recipes

class ToggleFavouriteView(View):
    """
    Add or remove recipe from favourites
    """
    def post(self, request, *args, **kwargs):
        recipe_id = self.kwargs['pk']
        recipe = get_object_or_404(Recipe, pk=recipe_id)
        recipe.is_favourite = not recipe.is_favourite
        recipe.save()
        return HttpResponseRedirect(reverse('full_recipe', args=[recipe_id]))


@login_required
def toggle_favourite(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)

    # Check if the user has already favorited the recipe
    if request.user in recipe.favorited_by.all():
        recipe.favorited_by.remove(request.user)
    else:
        recipe.favorited_by.add(request.user)

    return redirect('full_recipe', pk=pk)