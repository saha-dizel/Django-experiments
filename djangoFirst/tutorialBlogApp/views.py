from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Alex K',
        'title': 'Blog Post 1',
        'content': 'This is a very much dummy post. Enjoy it, while you can, though :)',
        'date_posted': 'January 20, 2020'
    },
    {
        'author': 'Dio Brando',
        'title': 'ZA WARUDO',
        'content': 'YOU THOUGHT IT WAS A REGULAR DUMMY POST? BUT IT WAS ME, DIO!!',
        'date_posted': 'January 20, 2020',
        'image': 'https://i.ytimg.com/vi/rduox9svDUQ/maxresdefault.jpg'
    }
]

# Create your views here.
def home(request):
    #return HttpResponse('<h1>Test for blog home</h1>')
    context = {
        'posts': posts
    }
    return render(request, 'tutorialBlogApp/home.html', context)


def about(request):
    #return HttpResponse('<h1>ABOUT</h1>')
    return render(request, 'tutorialBlogApp/about.html', {'title':'About page'})