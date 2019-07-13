from django.shortcuts import render
from django.views.generic import (View, TemplateView, ListView,
                                  DetailView, CreateView,
                                  UpdateView, DeleteView)


class index(TemplateView) :
    template_name = 'catalog/index.html'