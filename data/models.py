from django.db import models
from datetime import datetime

# Create your models here.
class Datapoint(models.Model):
    submit_date = models.DateTimeField(default=datetime.now, blank=False)
    value = models.BigIntegerField(blank=False)
    # Add in a 'which fountain button'? 
    def __str__(self):
        return str(self.value)