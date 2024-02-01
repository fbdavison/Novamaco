from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from user.form import AccountAuthenticationForm
from django.contrib.auth.models import Group
from django.http import HttpResponse


def login_user(request):
    user = request.user
    fail = False
    if user.is_authenticated:
        return redirect('index')
    if request.method == 'POST':
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)
            print(user)
            if user:
                login(request, user)
            return redirect('index')
        else:
            fail = True
            print(form.is_valid())
            print(fail)
            context = {'form': form, 'fail': fail}
            return render(request, 'user/login.html', context)
    else:
        form = AccountAuthenticationForm()
    context = {'form': form, 'fail': fail}
    return render(request, 'user/login.html', context)


@login_required()
def home(request):
    title = 'Portal - Home'
    context = {'title': title}
    return render(request, 'index.html', context)