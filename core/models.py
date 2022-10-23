from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.



class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.pk}. {self.name}"

class Transaction(models.Model):
    amount = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    user = models.IntegerField() # imitation of a user, should be foreign field

class UserSavings(models.Model):
    user = models.IntegerField() # imitation of a user, should be foreign field
    amount = models.FloatField()
    

class PiggyBank(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    limit = models.IntegerField()
    acummulating_rate = models.FloatField()
    current_amount = models.FloatField(default=0)
    total_amout = models.FloatField(default=0)
    user = models.IntegerField() # imitation of a user, should be foreign field
    name = models.CharField(max_length=100)

