from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User as DjangoUser
from django.contrib.auth.hashers import make_password, check_password
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

from utils.utils import send_mail
from .models import Users


def login_page(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user_profile = user_profile = Users.objects.get(user__email=email)
        except Users.DoesNotExist:
            messages.error(request, "Пользователь с таким email не найден")
            return render(request, 'login.html')

        if user_profile.user.check_password(password):

            # Авторизация через сессию
            request.session['user_email'] = user_profile.user.email
            request.session['user_role'] = user_profile.role
            request.session['user_course'] = user_profile.course
            messages.success(request, "Вы успешно вошли")
            return render(request, 'accounts/student.html', {'user': user_profile})
        else:
            messages.error(request, "Неверный пароль")
            return render(request, 'login.html')

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

        # Валидация email
        try:
            validate_email(email)
        except ValidationError:
            messages.error(request, "Некорректный формат email")
            return redirect('/auth/register')

        # Проверка на существование email
        if Users.objects.filter(user__email=email).exists():
            messages.error(request, "Пользователь с таким email уже существует")
            return redirect('/auth/login')

        if password != confirm_password:
            messages.error(request, "Пароли не совпадают")
            return redirect('/auth/register')

        if len(password) < 8:
            messages.error(request, "Пароль должен содержать минимум 8 символов")
            return redirect('/auth/register')

        try:
            # Создаём Django User
            django_user = DjangoUser.objects.create_user(
                username=username,
                email=email,
                password=password
            )

            # Создаём профиль
            Users.objects.create(
                user=django_user,
                username=username,
                email=email,
                password=make_password(password),
                course=course,
                faculty=faculty
            )

            # Отправка письма
            try:
                send_mail(
                    subject="Қош келдіңіз! SduXODIM",
                    recipients=[email],
                    template_name='Notification/welcome.html',
                    context={'user_email': email, 'username': username},
                )
            except Exception:
                messages.warning(request, "Письмо не отправлено, но регистрация успешна")

            messages.success(request, "Регистрация успешна!")
            return redirect('/auth/login')

        except Exception as e:
            print(e)
            messages.error(request, "Ошибка при регистрации. Попробуйте снова.")
            return redirect('/auth/register')

    return render(request, 'register.html')

