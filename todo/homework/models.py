import numbers
from django.db import models

# Create your models here.
class ToMeet(models.Model):
    persone=models.CharField(max_length=100)
    phone_number=models.CharField(max_length=10)
    date_of_meeting=models.DateTimeField(auto_now_add=True)
    comment=models.CharField(max_length=200)
    is_closed=models.BooleanField(default=False)
    is_favorite=models.BooleanField(default=False)
    
    