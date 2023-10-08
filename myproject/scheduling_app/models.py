from django.contrib.auth.models import User
from django.db import models
import random
import string

class Event(models.Model):
    event_name = models.CharField(max_length=255)
    event_date = models.DateField()
    event_time = models.TimeField()
    event_code = models.CharField(max_length=8, unique=True)
    organizer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def generate_event_code(self):
        # ランダムな8桁のアルファベット大文字、小文字、数字の組み合わせを生成
        return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(8))

    def save(self, *args, **kwargs):
        if not self.event_code:
            self.event_code = self.generate_event_code()
        super(Event, self).save(*args, **kwargs)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    display_name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.user.username