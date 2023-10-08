from django import forms
from .models import Event, UserProfile

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['event_name', 'event_date', 'event_time']
        widgets = {
            'event_date': forms.DateInput(attrs={'type': 'text', 'class': 'datepicker'}),
            'event_time': forms.TimeInput(attrs={'type': 'time'}),
        }

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['display_name']
