from django.contrib.auth.models import User
from django.db import models
import random
import string

class EventDate(models.Model):
    date = models.DateField()

class Event(models.Model):
    event_name = models.CharField(max_length=255)
    event_dates = models.ManyToManyField('EventDate', related_name='events')
    event_code = models.CharField(max_length=32, unique=True)
    event_organizer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    event_comment = models.TextField(max_length=65535, blank=True, null=True)

    def generate_event_code(self):
        # ランダムな32桁のアルファベット大文字、小文字、数字の組み合わせを生成
        return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(32))

    def save(self, *args, **kwargs):
        if not self.event_code:
            self.event_code = self.generate_event_code()
        super(Event, self).save(*args, **kwargs)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    display_name = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.user.username