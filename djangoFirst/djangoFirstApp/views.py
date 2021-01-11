from django import views
from django.http import HttpResponse


class HelloWorldView(views.View):
    def get(self, request):
        return HttpResponse('Hello World!')
