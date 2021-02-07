from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from userManagerApp import views as register_views
from .views import HomeViewClass, PostViewClass, PostCreateClass, PostUpdateClass, PostDeleteClass, PostByAuthorViewClass

urlpatterns = [
    path('', HomeViewClass.as_view(), name='blog-home'),
    path('post/<int:pk>/', PostViewClass.as_view(), name='blog-post'),
    path('post/new/', PostCreateClass.as_view(), name='blog-create-post'),
    path('post/<int:pk>/edit/', PostUpdateClass.as_view(), name='blog-edit-post'),
    path('post/<int:pk>/delete/', PostDeleteClass.as_view(), name='blog-delete-post'),
    path('about/', views.about, name='blog-about'),
    path('register/', register_views.register_view, name='blog-register'),
    path('login/', auth_views.LoginView.as_view(template_name='userManagerApp/login.html'), name='blog-login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='userManagerApp/logout.html'), name='blog-logout'),
    path('profile/', register_views.user_profile, name='blog-profile'),
    path('user/<str:username>', PostByAuthorViewClass.as_view(), name='blog-post-by-author')
]
