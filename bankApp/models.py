from django.db import models

# Create your models here.
class Account (models.Model):
    Identifier = models.CharField(max_length=255,null=True, blank=True)
    name = models.CharField(("name"), max_length=255,null=True, blank=True)
    balance = models.FloatField(("balane"),null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set the field to now when the object is first created

    def __str__(self):
        return self.name