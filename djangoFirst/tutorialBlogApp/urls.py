from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from userManagerApp import views as register_views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('register/', register_views.register_view, name='blog-register'),
    path('login/', auth_views.LoginView.as_view(template_name='userManagerApp/login.html'), name='blog-login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='userManagerApp/logout.html'), name='blog-logout'),
    path('profile/', register_views.user_profile, name='blog-profile')
]
