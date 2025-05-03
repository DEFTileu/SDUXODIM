# accounts/views.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from authentication.models import Users
from main.models import Event

@login_required
def profile(request):
    user = request.user
    events = Event.objects.all()

    try:
        profile = user.profile  # Получаем связанную модель Users
        if profile.role == 'student':
            return render(request, 'accounts/student.html', {'user': user, 'events': events})
        elif profile.role == 'club_head':
            return render(request, 'accounts/headofclub.html', {'user': user, 'events': events})
        else:
            return redirect('register/')
    except Users.DoesNotExist:
        # Если профиля нет, перенаправляем на регистрацию
        return redirect('register/')