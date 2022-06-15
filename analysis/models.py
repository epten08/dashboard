from django.db import models
from django import forms

# Create your models here.

class Sale(models.Model):
    DocDate = models.DateField(null=True,blank=True)
    DocNo = models.CharField(max_length=150,null=True)
    Customer = models.CharField(max_length=150,null=True)
    ProductCode = models.CharField(max_length=150,null=True)
    ProductName = models.CharField(max_length=250,null=True)
    SalesUnit = models.CharField(max_length=150,null=True)
    SalesQty = models.IntegerField()

    def __str__(self):
        return self.ProductCode
    
    objects = models.Manager()