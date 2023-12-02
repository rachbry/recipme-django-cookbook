# from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import render

# Create your views here.
class Index(TemplateView):
    template_name = 'home/index.html'