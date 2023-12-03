# from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse_lazy

# Create your views here.
# class Index(TemplateView):
#     template_name = 'home/index.html'

class Index(View):
    template_name = 'home/index.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            # If the user is logged in, automatically redirect to 'my_recipes' page
            return redirect('my_recipes')  # Replace 'my_recipes' with the actual name of your desired URL pattern
        else:
            # If the user is not logged in, proceed with rendering the index page
            return render(request, self.template_name, {'user': request.user})