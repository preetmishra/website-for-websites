from django.urls import path
from catalog import views

app_name = 'catalog'

urlpatterns = [
    path('', views.Index.as_view(), name = 'index'),
    path('add/', views.WebsiteCreateView.as_view(), name = 'addwebsite')
]