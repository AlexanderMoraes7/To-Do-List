from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm


def login_view(request : HttpRequest):
    # if this is a POST request, we need to process the form data
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        auth = authenticate(request, username=username, password=password)
        if auth is not None:
            login(request, auth)
            return redirect('home')
        else:
            form = AuthenticationForm(request, data=request.POST)
    else:        
        form = AuthenticationForm()

    return render(request, "login.html", {"form": form})
