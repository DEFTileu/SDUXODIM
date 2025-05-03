from django.shortcuts import render
from main.models import Event
 
# Create your views here.
def index_page(request):
    all_events = Event.objects.all()
    print("All Events: ")
    for i, j in enumerate(all_events):
        print(i + 1, j)
    return render(request, 'index.html')


def about_page(request):
    return render(request, 'about.html')
