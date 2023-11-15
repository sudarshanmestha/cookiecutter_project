
from django.urls import path
from .views import detail, category, search



urlpatterns = [
    path('search/', search, name='search'),
    path('<slug:slug>/', category, name='category_detail'),
    path('<slug:category_slug>/<slug:slug>/', detail, name='post_detail'),
    
] 
