from django import forms
from catalog import models


class FilterByTagForm(forms.Form) :    
    tag = forms.ModelChoiceField(
        queryset=models.Tag.objects.filter(tags__isnull = False).distinct(),
        empty_label = 'All', 
        label = '', 
        required = False) 
        # required is set to false in order to use All filter using None returned by the post method
