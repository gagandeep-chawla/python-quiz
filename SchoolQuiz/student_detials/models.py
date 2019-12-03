from django.db import models
from django.contrib.auth.models import User 
# Create your models here.

class Student_Info(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE,related_name='student')
    name = models.CharField(max_length=255,unique=False,null=False,blank=False)
    standard = models.CharField(max_length=255,blank=False,null=False)
    roll_number = models.CharField(max_length=255,unique=True,null=False,blank=False)
    dob = models.DateField(auto_now=False,verbose_name='Birthday')
    score = models.IntegerField(default=0)
    difficulty_level = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name