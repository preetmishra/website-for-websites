from django.shortcuts import render
from django.views.generic import (View, TemplateView, ListView,
                                  DetailView, CreateView,
                                  UpdateView, DeleteView)
from catalog import models 

class index(ListView) :
    template_name = 'catalog/index.html'
    model = models.Website
    context_object_name = 'websites'