from django.shortcuts import render, get_object_or_404
from main.models import Event
from django.utils import timezone
from authentication.models import Users
import datetime
 
# Create your views here.
def index_page(request):
    all_events = Event.objects.all()
    for i in all_events:
        i.date = timezone.localtime(i.date)

    return render(request, 'index.html', context={'events': all_events})


def about_page(request):
    return render(request, 'about.html')

def register_page(request):
    return render(request, 'register.html')

def login_page(request):
    return render(request, 'login.html')

def booking_page(request):
    return render(request, 'booking.html')

def booking_view(request, event_id):
    now = datetime.datetime.now()
    event = get_object_or_404(Event, id=event_id)
    return render(request, 'booking.html', {'event': event})


from django.shortcuts import redirect
from django.contrib.auth import logout

def logout_view(request):
    logout(request)  # Выход пользователя
    return redirect('/')  # Перенаправление на главную страницу или на любую другую



import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Ticket, Event
from django.contrib.auth.decorators import login_required

import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect
from .models import Ticket, Event
from django.contrib.auth.decorators import login_required

@login_required
@csrf_protect  # Защита CSRF для POST-запроса
def place_order(request):
    if request.method == 'POST':
        try:
            # Получаем данные из JSON-запроса
            data = json.loads(request.body)
            event_id = data.get('event_id')
            ticket_count = data.get('ticket_count')

            # Получаем событие и пользователя
            event = Event.objects.get(id=event_id)
            user = request.user

            # Создаем билеты в базе данных
            for _ in range(ticket_count):
                Ticket.objects.create(user=user, event=event)

            # Возвращаем успешный ответ
            return JsonResponse({'success': True})

        except Exception as e:
            # В случае ошибки возвращаем сообщение об ошибке
            return JsonResponse({'success': False, 'error': str(e)})

    return JsonResponse({'success': False, 'error': 'Invalid request method'})



