from django.db import models
from app.managers import SalesQuerySet

class Sales(models.Model):
    region = models.CharField(max_length = 255)
    country = models.CharField(max_length=255)
    ptype = models.CharField(max_length=255)
    channel = models.CharField(max_length=255)
    date = models.DateField(auto_now=False)
    quantity = models.IntegerField()
    price = models.FloatField()
    cost = models.FloatField()
    revenue = models.FloatField()
    profit = models.FloatField()
    
    objects = SalesQuerySet.as_manager()