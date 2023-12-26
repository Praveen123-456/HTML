from django.db import models

# Create your models here.

class Employees(models.Model):
    name = models.CharField(max_length=255)
    time = models.CharField(max_length=255)
    salary = models.CharField(max_length=255)
