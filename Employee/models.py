from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=50, default="name")
    code = models.CharField(max_length=8, default="code")
    department = models.CharField(max_length=20, default="department")
        
    def __str__(self):
        return self.name
    
