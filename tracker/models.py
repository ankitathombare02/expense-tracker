from django.db import models

# Create your models here.

class Budget(models.Model):
    month = models.CharField(max_length=20)
    amount = models.FloatField()

class Expense(models.Model):
    category = models.CharField(max_length=50)
    amount = models.FloatField()
    date = models.DateField()