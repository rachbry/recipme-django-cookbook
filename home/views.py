from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse_lazy


class Index(View):
    template_name = 'home/index.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            # If logged in, automatically redirect to 'my_recipes' page
            return redirect('my_recipes')
        else:
            # If not logged in, render index page
            return render(request, self.template_name, {'user': request.user})
