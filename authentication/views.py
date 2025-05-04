from django.contrib.auth import authenticate
from .models import Users  # или accounts.models

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from utils.utils import send_mail
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Users

from django.contrib.auth import login

def login_page(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email, password)


        try:
            auth_user = Users.objects.get(email=email)
            print(auth_user)
            print(auth_user.password == password)
            print(auth_user.password)
            if auth_user.password == password:
                auth_user.backend = 'django.contrib.auth.backends.ModelBackend'
                print(auth_user)
                login(request, auth_user)

                request.session['user_email'] = auth_user.email
                messages.success(request, "Вы успешно вошли!")
                return redirect('index')

            else:
                messages.error(request, "Неверный пароль")
        except Users.DoesNotExist:
            messages.error(request, "Пользователь с таким email не найден")

    return render(request, 'login.html')




def register_page(request):
    if request.user.is_authenticated:
        return redirect('/profile')

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm-password')
        course = request.POST.get('course')
        faculty = request.POST.get('faculty')
        role = request.POST.get('role')

        try:
            validate_email(email)
        except ValidationError:
            messages.error(request, "Некорректный формат email")
            return redirect('/auth/register')

        if Users.objects.filter(email=email).exists():
            messages.error(request, "Пользователь с таким email уже существует")
            return redirect('/auth/login')

        if password != confirm_password:
            messages.error(request, "Пароли не совпадают")
            return redirect('/auth/register')

        if len(password) < 8:
            messages.error(request, "Пароль должен содержать минимум 8 символов")
            return redirect('/auth/register')

        try:

            Users.objects.create(
                username=username,
                email=email,
                password=password,
                course=course,
                faculty=faculty,
                role = role,
            ).save()


            try:
                send_mail(
                    subject="Қош келдіңіз! SduXODIM",
                    recipients=[email],
                    template_name='Notification/welcome.html',
                    context={'user_email': email, 'username': username},
                )
            except Exception as e:
                messages.warning(request, "Письмо не отправлено, но регистрация успешна")

            messages.success(request, "Регистрация успешна!")
            return redirect('/auth/login')

        except Exception as e:
            messages.error(request, "Ошибка при регистрации. Попробуйте снова.")
            print(e)
            return redirect('/auth/register')

    return render(request, 'register.html')
