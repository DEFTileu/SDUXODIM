from django.shortcuts import render, get_object_or_404

import accounts.forms
from main.models import Event
from django.utils import timezone
from authentication.models import Users
import datetime
    
 
# Create your views here.
from django.utils import timezone
from authentication.models import Users
from main.models import Event

def index_page(request):
    email = request.session.get('user_email')
    user = None

    if email is not None:
        try:
            user = Users.objects.get(email=email)
        except Users.DoesNotExist:
            user = None  # Вдруг email есть в сессии, но пользователь был удалён

    all_events = Event.objects.all()
    for i in all_events:
        i.date = timezone.localtime(i.date)

    return render(request, 'index.html', context={'user': user, 'events': all_events})



def about_page(request):
    return render(request, 'about.html')

def register_page(request):
    return render(request, 'register.html')

def login_page(request):
    return render(request, 'login.html')

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


@csrf_protect  # Защита CSRF для POST-запроса
def place_order(request):
    email = request.session.get('user_email')
    user = None

    if email is not None:
        if request.method == 'POST':
            try:
                user = request.user
                # Получаем данные из JSON-запроса
                data = json.loads(request.body)
                event_id = data.get('event_id')
                ticket_count = data.get('ticket_count')

                # Получаем событие и пользователя
                event = accounts.forms.EventForm.save(commit=False)
                event.creator = request.user  # <- связываем с текущим пользователем
                event.save()

                # Создаем билеты в базе данных
                for _ in range(ticket_count):
                    Ticket.objects.create(user=user, event=event)

                # Возвращаем успешный ответ
                return JsonResponse({'success': True})

            except Exception as e:
                # В случае ошибки возвращаем сообщение об ошибке
                return JsonResponse({'success': False, 'error': str(e)})

    return JsonResponse({'success': False, 'error': 'Invalid request method'})


from django.shortcuts import get_object_or_404

from django.http import HttpResponseForbidden

def event_detail(request, event_id):
    email = request.session.get('user_email')
    user = None

    if email is not None:
        event = get_object_or_404(Event, title=event_id, creator=request.user)
        print(event)
        return render(request, 'event_detail.html', {'event': event})
    else:
        return HttpResponseForbidden("Вы должны войти, чтобы просматривать это событие.")
