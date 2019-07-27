from django.urls import path
from catalog import views

app_name = 'catalog'

urlpatterns = [
    path('', views.Index.as_view(), name = 'index'),
    path('add/', views.WebsiteCreateView.as_view(), name = 'addwebsite'),
    path('about/', views.AboutView.as_view(), name = 'about'),
    path('howitworks/', views.HowItWorksView.as_view(), name = 'howitworks'),
]