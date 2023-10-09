from django import forms
from .models import Event, UserProfile

class EventForm(forms.ModelForm):
    event_dates = forms.DateField(widget=forms.HiddenInput())  # 非表示のDateField

    class Meta:
        model = Event
        fields = ['event_name', 'event_dates', 'event_comment']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['display_name']
