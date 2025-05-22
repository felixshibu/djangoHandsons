from django.db import models

# Create your models here.
class InventoryModel(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    price = models.IntegerField()
    discount = models.IntegerField()
    quantity = models.IntegerField()
    barcode = models.IntegerField(unique=True)


