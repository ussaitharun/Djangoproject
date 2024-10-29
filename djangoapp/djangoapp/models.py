from django.db import models
from django.utils import timezone
import datetime

class Products(models.Model):
    name = models.CharField(max_length=255)  
    detail = models.TextField()   
    learning_percentage = models.IntegerField(default=0)
