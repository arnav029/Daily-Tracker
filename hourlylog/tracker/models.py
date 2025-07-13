from django.db import models

from django.contrib.auth.models import User

class DayLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()

    class Meta:
        unique_together = ('user', 'date')  # 1 log per user per day

class HourLog(models.Model):
    day = models.ForeignKey(DayLog, related_name='logs', on_delete=models.CASCADE)
    hour = models.IntegerField()
    content = models.TextField(blank=True)

