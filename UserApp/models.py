from django.db import models
from AdminApp.models import Kadai,Answer,Material,KadaiProgress
from django.contrib.auth.models import User

class Test(models.Model):
    kadai = models.ForeignKey(Kadai, related_name="tests", on_delete=models.CASCADE, verbose_name="問題",to_field="number")
    
        
