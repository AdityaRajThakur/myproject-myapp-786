from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.



class RenderView(TemplateView):
    template_name = 'myapp/index.html' 
    