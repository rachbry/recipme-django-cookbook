from django import forms
from djrichtextfield.widgets import RichTextWidget
from .models import Recipe


class RecipeForm(forms.ModelForm):
    """
    Form to create a recipe
    """
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'ingredients', 'instructions', 'image', 'image_alt', 'recipe_types', 'cooking_method', 'servings', 'freezable',]

        # ingredients = forms.CharField(widget=RichTextWidget())
        # instructions = forms.CharField(widget=RichTextWidget())

        widgets = {
            'description': forms.Textarea(attrs={'rows':5}),
        }

        labels = {
            'title': 'Recipe Title', 
            'description': 'Recipe Description',
            'ingredients': 'Recipe Ingredients',
            'instructions': 'Recipe Instructions',
            'image': 'Recipe Image',
            'image_alt': 'Describe Image',
            'recipe_types': 'Recipe Type',
            'cooking_method': 'Coking Method',
            'servings': 'Servings',
            'freezable': 'Freezable?',
        }

        # Prepopulate the slug
    def save(self, commit=True):
        instance = super(RecipeForm, self).save(commit=False)

        instance.slug = instance.title.lower().replace(' ', '-')

        if commit:
            instance.save()

        return instance

