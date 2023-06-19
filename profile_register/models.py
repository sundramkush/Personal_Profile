from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class profile(models.Model):
    name = models.CharField(max_length=100)
    past_address = models.CharField(max_length=100)  
    current_address = models.CharField(max_length=100)
    ph_number = models.CharField(max_length=15)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
