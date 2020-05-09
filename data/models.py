from django.db import models
from datetime import datetime

# Create your models here.
class Datapoint(models.Model):
    timestamp = models.TextField(default=datetime.now(), blank=False)
    date = models.TextField(default=datetime.date(datetime.now()), blank=False)
    time = models.TextField(default=datetime.time(datetime.now()), blank=False)
    value = models.BigIntegerField(blank=False)
    cumulative = models.BigIntegerField(blank=False)

    # Add in a 'which fountain button'? 
    def __str__(self):
        return str(self.value)+ "," + self.timestamp
    pass