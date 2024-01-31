from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from user.form import AccountAuthenticationForm
from django.contrib.auth.models import Group
from django.http import HttpResponse


def login_user(request):
    user = request.user
    if user.is_authenticated:
        return redirect('tier_welcome')
    if request.method == 'POST':
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
            return redirect('index')
    else:
        form = AccountAuthenticationForm()
    context = {'form': form}
    return render(request, 'user/login.html', context)
