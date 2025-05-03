from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from utils.utils import send_mail

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, "Неверные данные")
    return render(request, 'login.html')

def register_page(request):
    if request.method == 'POST':
        username = request.POST.get("User name")
        email = request.POST.get("Email")
        password = request.POST.get("Password")
        send_mail(
            subject="Қош келдіңіз! SduXODIM",
            recipients=[email],
            template_name='welcome.html',
            context={'user_email': email},
        )
    return render(request, 'register.html')

def logout_page(request):
    logout(request)
    return redirect('/auth/login/')
