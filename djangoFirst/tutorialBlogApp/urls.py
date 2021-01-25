from django.urls import path
from . import views
from userManagerApp import views as register_views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('register/', register_views.register_view, name='blog-register')
]