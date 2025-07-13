from django.db import models

class DayLog(models.Model):
    date = models.DateField(unique=True)

class HourLog(models.Model):
    day = models.ForeignKey(DayLog, related_name='logs', on_delete=models.CASCADE)
    hour = models.IntegerField()  # 0 to 23
    content = models.TextField(blank=True)
