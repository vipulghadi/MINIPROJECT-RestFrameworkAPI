from django.db import models

# Create your models here.
class StudentProfile(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    nickname=models.CharField(max_length=100)
    
    def __str__(self):
        return self.name