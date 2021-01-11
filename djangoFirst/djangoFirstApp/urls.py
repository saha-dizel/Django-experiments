from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.HelloWorldView.as_view())
]
