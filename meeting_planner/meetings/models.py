from django.db import models
from datetime import time , datetime

class Meeting(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField(default=datetime.now())
    start_time = models.TimeField(default=time(9))
    duration = models.IntegerField(default=1)


