from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class TemplateView1(TemplateView):
    template_name = 'blog/index.html'