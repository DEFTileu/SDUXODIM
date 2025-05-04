from django import forms
from main.models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'organizer', 'date', 'location']
        widgets = {
            'date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
        labels = {
            'title': 'Название',
            'organizer': 'Организатор (клуб)',
            'date': 'Дата и время',
            'location': 'Место проведения',
        }
