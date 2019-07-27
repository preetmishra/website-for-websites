from django.shortcuts import render
from django.views.generic import (
    TemplateView,
    CreateView,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from catalog import models 
from catalog import forms

class Index(TemplateView) :
    template_name = 'catalog/index.html'

    def get(self, request, *args, **kwargs) :
        websites = models.Website.objects.filter(approved = 'True')
        tag_form = forms.FilterByTagForm()
        if request.user.id :
            user_id = request.user.id
            favourites = models.UserProfile.objects.get(user_id = user_id).favourites.all()
            return render(request, self.template_name, {'tag_form': tag_form, 
                                                        'websites': websites, 
                                                        'favourites': favourites})
        else :
            return render(request, self.template_name, {'tag_form': tag_form,
                                                        'websites': websites})

    def post(self, request, *args, **kwargs) :
        tag_form = forms.FilterByTagForm(request.POST)
        if tag_form.is_valid() :
            if tag_form.cleaned_data['tag'] == None :
                websites = models.Website.objects.filter(approved = 'True')
                return render(request, self.template_name, {'tag_form': tag_form, 'websites': websites})
            else :
                tag_id = tag_form.cleaned_data['tag'].id
                websites = models.Website.objects.filter(approved = 'True').filter(tag_id = tag_id)
                return render(request, self.template_name, {'tag_form': tag_form, 'websites': websites})


class WebsiteCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = models.Website
    fields = ['name', 'url', 'tag']

    success_url = reverse_lazy('catalog:index')
    success_message = "Thank you for contributing! We have recieved your request. We will add your suggested website as soon as we are done with its verification."
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(WebsiteCreateView, self).form_valid(form)

class AboutView(TemplateView) :
    template_name = 'catalog/about.html'

class HowItWorksView(TemplateView) :
    template_name = 'catalog/howitworks.html'
