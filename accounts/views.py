# accounts/views.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from authentication.models import Users
from main.models import Event

@login_required
def profile(request):
    email = request.session.get('user_email')
    if not email:
        return redirect('login')

    try:
        user = Users.objects.get(email=email)
        events = Event.objects.all()

        if user.role == 'student':
            return render(request, 'accounts/student.html', {'user': user, 'events': events})
        elif user.role == 'club_head':
            return render(request, 'accounts/headofclub.html', {'user': user, 'events': events})
        else:
            return redirect('register')
    except Users.DoesNotExist:
        return redirect('register')