from django.db import models

# Create your models here.
class Account (models.Model):
    name = models.CharField(("name"), max_length=255)
    balance = models.FloatField(("balane"))