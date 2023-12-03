from django.db.models import Q 

# search bar parameters
def get_queryset_with_query(model, query, user=None): 
    # Ensure query is a string, even if it's empty 
    query = query or '' 
    base_query = ( 
        Q(title__icontains=query) | 
        Q(description__icontains=query) | 
        Q(instructions__icontains=query) | 
        Q(ingredients__icontains=query) | 
        Q(recipe_types__icontains=query) | 
        Q(cooking_method__icontains=query) 
        ) 

    if user: 
        return model.objects.filter(base_query, Q(user=user)) 
# removed from the end of inside the line above
#  | Q(is_favourite=True)
    else: 
        return model.objects.filter(base_query) 