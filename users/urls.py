from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from users import views as user_views
from django.contrib.auth import views as auth_views

app_name = 'users'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name = 'users/login.html'), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', user_views.register , name='register'),
    path('profile/', user_views.ProfileView.as_view(), name='profile'),
    path('profile/update/', user_views.update_profile_view, name='updateprofile'),
    path('favourites/<str:operation>/<int:pk>', user_views.tweak_favourites, name='tweakfavourites')
] 

if settings.DEBUG :
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
