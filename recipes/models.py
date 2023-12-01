from django.db import models
from django.contrib.auth.models import User
from djrichtextfield.models import RichTextField
from django_resized import ResizedImageField

# Choice fields
RECIPE_TYPES = (
    ('baking', 'Baking'),
    ('breakfast', 'Breakfast'),
    ('drinks', 'Drinks'),
    ('main meal', 'Main Meal'),
    ('sauces', 'Sauces'),
    ('sides', 'Sides'),
    ('snacks', 'Snacks'),
    ('spice-mix', 'Spice Mix'),
    ('misc', 'Misc'),
)

COOKING_METHOD =  (
    ('air fryer', 'Air Fryer'),
    ('bbq', 'BBQ'),
    ('hob', 'Hob'),
    ('no cook', 'No Cook'),
    ('oven', 'Oven'),
    ('pressure cooker', 'Pressure Cooker'),
    ('slow cooker', 'Slow Cooker'),
    ('other', 'Other'),
)

# Create your models here.
class Recipe(models.Model):
    """
    Model to create and manage recipes
    """
    user = models.ForeignKey(User, related_name='recipe_owner', on_delete=models.CASCADE)
    title = models.CharField(max_length=300, null=False, blank=False)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.CharField(max_length=500, null=False, blank=False)
    instructions = RichTextField(max_length=10000, null=False, blank=False)
    ingredients = RichTextField(max_length=10000, null=False, blank=False)
    image = ResizedImageField(
        size=[400, None], quality=75, upload_to='recipes/', force_format='WEBP', blank=False, null=False
    )
    image_alt = models.CharField(max_length=100, null=False, blank=False)
    # dropdowns
    recipe_types = models.CharField(max_length=50, choices=RECIPE_TYPES, default='baking')
    cooking_method = models.CharField(max_length=50, choices=COOKING_METHOD, default='air fryer')

    servings = models.CharField(max_length=100, null=False, blank=False)
    posted_date = models.DateTimeField(auto_now=True)

    freezable = models.BooleanField(default=False)

    class Meta:
        ordering = ['-posted_date']

    def __str__(self):
        return str(self.title)