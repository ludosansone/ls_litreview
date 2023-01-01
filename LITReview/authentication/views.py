from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from authentication.forms import LoginForm


def signin(request):
    form = LoginForm()
    error = ''

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                error = "Nom d'utilisateur ou mot de passe incorrect"
    return render(request, 'authentication/signin.html', {'form': form, 'error': error})


def signup(request):
    return render(request, 'authentication/signup.html')


def signout(request):
    logout(request)
    return redirect('signin')
