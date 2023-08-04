from django.db import models

# Create your models here.

class EmployeeModel(models.Model):
    f_name = models.CharField(max_length=30)
    l_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    
    