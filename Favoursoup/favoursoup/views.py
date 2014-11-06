from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import logout

# Create your views here.

def home(request):
    if request.user.is_authenticated():
       return redirect('done')
    return render(request, 'home.html', {})

@login_required
def done(request):

    return render(request, 'done.html', {})

def logout_view(request):
    logout(request)
    return redirect('home')

def signup(request):
    return render(request, 'signup.html', {})

def signin(request):
    return render(request, 'signin.html', {})
