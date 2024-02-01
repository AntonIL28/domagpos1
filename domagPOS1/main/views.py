from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from main.forms import RegisterForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def modulos (request):

    return render(request, 'modulos.html',{
        'title': 'Menú Principal'
    })

def register_page(request):

    register_form = RegisterForm()

    if request.method == 'POST':
        register_form = RegisterForm(request.POST)

        if register_form.is_valid():
            register_form.save()

            return redirect('/')


    return render(request, 'users/register.html',{
        'title': 'Registrarse',
        'register_form' : register_form
    })

def login_page(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        
        else:
            messages.warning(request, 'No te has identificado correctamente!!')
            return redirect('login')

    return render(request, 'users/login.html',{
        'title' : 'Identificate'
    })

def logout_user(request):

    logout(request)
    return redirect('login')
