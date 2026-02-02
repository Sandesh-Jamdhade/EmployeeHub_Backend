from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    department = models.CharField(max_length=50)
    salary = models.IntegerField()

