from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account successfully created for {username}! You can now log in! Yay!')
            return redirect('blog-login')
    else:
        form = UserRegistrationForm()
    return render(request, 'userManagerApp/register.html', {'form': form})

@login_required
def user_profile(request):
    return render(request, 'userManagerApp/profile.html')
