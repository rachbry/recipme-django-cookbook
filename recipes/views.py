from django.shortcuts import render
from django.views.generic import CreateView
from .models import Recipe
from .forms import RecipeForm
from django.contrib.auth.mixins import LoginRequiredMixin

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