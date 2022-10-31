from django.db import models

# Create your models here.


class Order(models.Model):
    number = models.IntegerField()
    type = models.CharField()
    weight = models.IntegerField()
    shipment_date = models.DateField()
    shipping_date = models.DateField()
    status = models.IntegerField(null=True)
    