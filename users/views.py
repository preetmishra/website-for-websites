from django.shortcuts import render, redirect
from django.contrib import messages 
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from users import forms
from catalog import models

# Create your views here.

def register(request) :

    if request.user.is_authenticated : 
        return redirect('catalog:index')

    if request.method == 'POST' :
        user_form = forms.UserForm(data = request.POST)
        user_profile_form = forms.UserProfileForm(data = request.POST)

        if user_form.is_valid() and user_profile_form.is_valid() :

            username = user_form.cleaned_data.get('username')
            messages.success(request, f'Congratulations! You are successfully registered as {username}.')
            user = user_form.save()
            
            # Password Hashing
            user.set_password(user.password)
            user.save()

            profile = user_profile_form.save(commit = False)
            
            # We need to state one to one relation before saving
            profile.user = user
            
            if 'profile_picture' in request.FILES :
                profile.profile_picture = request.FILES['profile_picture']

            profile.save()

            return redirect('users:login')
        
        else :
            pass
    else :
        user_form = forms.UserForm()
        user_profile_form = forms.UserProfileForm()

    return render(request, 'users/register.html', {'user_form' : user_form, 
                                                    'user_profile_form' : user_profile_form })

class ProfileView(LoginRequiredMixin, TemplateView) :
    template_name = 'users/profile.html'

    def get(self, request, *args, **kwargs) :
        user_id = request.user.id
        favourites = models.UserProfile.objects.get(user_id = user_id).favourites.all()
        return render(request, self.template_name, {'favourites' : favourites })

@login_required
def tweak_favourites(request, operation, pk) :
    models.UserProfile.add_or_remove_favourites(user_id = request.user.id, website_id = pk, operation = operation)
    website = models.Website.objects.get(id = pk)
    if operation == 'add' :
        messages.info(request, f'Successfully added {website} to your favourites.')
    elif operation == 'remove' :
        messages.warning(request, f'Removed {website} from your favourites.')
    return redirect('catalog:index')


@login_required
def update_profile_view(request) :
    
    if request.method == 'POST' :
        user_update_form = forms.UserUpdateForm(request.POST, instance = request.user)
        user_profile_update_form = forms.UserProfileUpdateForm(request.POST,
                                                                request.FILES,
                                                                instance = request.user.profile)
        if user_update_form.is_valid and user_profile_update_form.is_valid :
            user_update_form.save()
            user_profile_update_form.save()
            messages.success(request, f'Your profile has been updated successfully!')
            return redirect('users:profile')
    else :
        user_update_form = forms.UserUpdateForm(instance = request.user)
        user_profile_update_form = forms.UserProfileUpdateForm(instance = request.user.profile)

    return render(request, 'users/update_profile.html', {'user_update_form' : user_update_form,
                                                'user_profile_update_form' : user_profile_update_form})
