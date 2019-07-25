from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password, password_validators_help_text_html
from catalog import models

class UserForm(forms.ModelForm) :
    password = forms.CharField(widget=forms.PasswordInput(), 
                                help_text = password_validators_help_text_html)
    confirm_password = forms.CharField(widget=forms.PasswordInput(), 
                                help_text='Enter the same password as before, for verification.')
    email = forms.EmailField(required = True, help_text = 'Required.')

    class Meta :
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']

    def clean(self) :
        cleaned_data = super(UserForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("Password did not match.")

        validate_password(confirm_password, self.instance)

        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if email and User.objects.filter(email=email).exclude(username=username).exists():
            raise forms.ValidationError(u'Email addresses must be unique.')


class UserProfileForm(forms.ModelForm) :
    class Meta :
        model =  models.Profile
        fields = ['gender', 'profile_picture']

class UserUpdateForm(forms.ModelForm) :
    class Meta :
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']

        def clean(self):
            cleaned_data = super(UserForm, self).clean()
            email = self.cleaned_data.get('email')
            username = self.cleaned_data.get('username')
            if email and User.objects.filter(email=email).exclude(username=username).exists():
                raise forms.ValidationError(u'Email addresses must be unique.')

class UserProfileUpdateForm(forms.ModelForm):
    class Meta :
        model = models.Profile
        fields = ['gender', 'profile_picture']
