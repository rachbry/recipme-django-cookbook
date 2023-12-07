from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import (
    UserPassesTestMixin, LoginRequiredMixin
)
from django.core.exceptions import PermissionDenied
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import View
from django.views.generic import (
    CreateView, ListView, DetailView, DeleteView, UpdateView
)
from django.contrib.messages.views import SuccessMessageMixin

from .utils import is_favourite
from .models import Recipe
from .forms import RecipeForm


class AddRecipe(LoginRequiredMixin, CreateView):
    """
    Add recipe view
    """
    template_name = 'recipes/add_recipe.html'
    model = Recipe
    form_class = RecipeForm
    success_url = '/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "Recipe added successfully!")
        return super().form_valid(form)


class Recipes(ListView):
    """
    View all recipes
    """
    template_name = 'recipes/recipes.html'
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
            recipes = self.model.objects.all()

        # Add is_favourite field to each recipe in the queryset
        if user.is_authenticated:
            for recipe in recipes:
                recipe.is_favourite = is_favourite(user.id, recipe.id)

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

        filtered_recipes = recipes.filter(
            Q(user=user) | Q(user__is_staff=True))

        # Add is_favourite field to each recipe in the queryset
        for recipe in filtered_recipes:
            recipe.is_favourite = is_favourite(user.id, recipe.id)

        return filtered_recipes


class FullRecipe(DetailView):
    """
    View full detail for single a recipe
    """
    template_name = 'recipes/full_recipe.html'
    model = Recipe
    context_object_name = 'recipe'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        recipe = context['recipe']

        # Check if the current user has favorited this recipe
        fav = recipe.favourites.filter(id=self.request.user.id).exists()

        # Add the 'fav' variable to the context
        context['fav'] = fav

        return context


class EditRecipe(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    Edit a recipe
    """
    template_name = 'recipes/edit_recipe.html'
    model = Recipe
    form_class = RecipeForm
    success_url = '/recipes'

    def test_func(self):
        return (
            self.request.user.is_authenticated
            and self.request.user == self.get_object().user
        )

    def handle_no_permission(self):
        raise PermissionDenied(
            "You do not have permission to edit this recipe."
            )

    def handle_exception(self, exc):
        if isinstance(exc, PermissionDenied):
            messages.error(
                self.request, "You do not have permission to edit this recipe."
                )
            return render(self.request, '403.html', status=403)
        return HttpResponseForbidden()

    def form_valid(self, form):
        messages.success(self.request, 'Recipe updated successfully!')
        return super().form_valid(form)

    def get_success_url(self):
        return self.request.path


class DeleteRecipe(
        LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    Deletes a recipe
    """
    model = Recipe
    success_url = '/'

    def test_func(self):
        return self.request.user == self.get_object().user

    def handle_no_permission(self):
        # Raise a PermissionDenied exception
        raise PermissionDenied(
            "You do not have permission to delete this recipe.")

    def handle_exception(self, exc):
        # Handle PermissionDenied exception and redirect to 403.html
        if isinstance(exc, PermissionDenied):
            messages.error(
                self.request,
                "You do not have permission to delete this recipe.")

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

        # Add is_favourite field to each recipe in the queryset
        if user.is_authenticated:
            for recipe in recipes:
                recipe.is_favourite = is_favourite(user.id, recipe.id)
        return recipes


@login_required
def favourite_add(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    if recipe.favourites.filter(id=request.user.id).exists():
        recipe.favourites.remove(request.user)
        messages.success(
            request, 'Recipe removed from favorites successfully!')
    else:
        recipe.favourites.add(request.user)
        messages.success(
            request, 'Recipe added to favorites successfully!')
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def favourite_list(request):
    user_favourite_recipes = Recipe.objects.filter(favourites=request.user)
    return render(
        request, 'recipes/favourite_recipes.html',
        {'user_favourite_recipes': user_favourite_recipes})