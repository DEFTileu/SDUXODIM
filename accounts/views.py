from django.shortcuts import render, redirect
from authentication.models import Users
from main.models import Event

def profile(request):
    email = request.session.get('user_email')

    # Если email отсутствует в сессии — пользователь не вошёл
    if not email:
        return redirect('login')

    try:
        # Пытаемся найти пользователя в базе
        user = Users.objects.get(email=email)

        # Дополнительная проверка, если нужно (например, активность)
        # if not user.is_active:
        #     return redirect('register')

        events = Event.objects.all()

        if user.role == 'student':
            return render(request, 'accounts/student.html', {'user': user, 'events': events})
        elif user.role == 'club_head':
            return render(request, 'accounts/headofclub.html', {'user': user, 'events': events})
        else:
            return redirect('register')

    except Users.DoesNotExist:
        # Если пользователь не найден в базе
        return redirect('register')


from django.shortcuts import render, redirect
from .forms import EventForm
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from .forms import EventForm

def add_event(request):
    email = request.session.get('user_email')

    # Если email отсутствует в сессии — пользователь не вошёл
    if not email:
        return redirect('login')
    # URL name для страницы входа

    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            # Если хочешь привязать пользователя как создателя — добавь поле в модель
            event.save()
            return redirect('profile')  # URL name для профиля
    else:
        form = EventForm()

    return render(request, 'add_event.html', {'form': form})
