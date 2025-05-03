from django.shortcuts import render
from main.models import Event
 
# Create your views here.
def index_page(request):
    all_events = Event.objects.all()
    array = []
    for i in all_events:
        array.append([i.title, i.organizer])
    data = dict(array)
    return render(request, 'index.html', context={'events': all_events})


def about_page(request):
    return render(request, 'about.html')

def register_page(request):
    return render(request, 'register.html')

def login_page(request):
    return render(request, 'login.html')