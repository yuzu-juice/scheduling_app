from django import forms
from django.core.exceptions import ValidationError
from .models import Event, UserProfile
from datetime import datetime

# カスタムバリデータの関数を定義
def validate_date_list_format(value):
    date_strings = value.split(',')
    for date_str in date_strings:
        try:
            # 日付文字列をdatetimeオブジェクトに変換し、正しいフォーマットであるか確認
            datetime.strptime(date_str.strip(), '%Y-%m-%d')
        except ValueError:
            raise ValidationError('Invalid date format. Use yyyy-mm-dd,yyyy-mm-dd,... format.')


class EventForm(forms.ModelForm):
    event_dates = forms.CharField(
        widget=forms.HiddenInput(attrs={'class': 'event-dates'}),
        validators=[validate_date_list_format]  # カスタムバリデータを指定
    )

    class Meta:
        model = Event
        fields = ['event_name', 'event_dates', 'event_comment']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['display_name']
