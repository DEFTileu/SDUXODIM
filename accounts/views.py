# accounts/views.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from authentication.models import Users
from main.models import Event

@login_required
def profile(request):
    email = request.user.email  # email пользователя в стандартной модели User

    try:
        # Ищем пользователя в модели Users по email
        user = Users.objects.get(email=email)
        events = Event.objects.all()

        # Проверяем роль пользователя и возвращаем соответствующий шаблон
        if user.role == 'student':
            return render(request, 'accounts/student.html', {'user': user, 'events': events})
        elif user.role == 'club_head':
            return render(request, 'accounts/headofclub.html', {'user': user, 'events': events})
        else:
            return redirect('register/')  # Если роль не определена, перенаправляем на страницу регистрации
    except Users.DoesNotExist:
        # Если пользователь не найден в базе данных, перенаправляем на страницу регистрации
        return redirect('register/')