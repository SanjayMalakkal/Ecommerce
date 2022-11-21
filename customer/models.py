from django.db import models

from common.models import Customer, Seller
from seller.models import Product

# Create your models here.

class Cart(models.Model):
    customer = models.ForeignKey(Customer,on_delete = models.CASCADE)
    product = models.ForeignKey(Product,on_delete = models.CASCADE)

class Orders(models.Model):
    customer = models.ForeignKey(Customer,on_delete = models.CASCADE)
    product = models.ForeignKey(Product,on_delete = models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    delivery_status = models.CharField(max_length=100)
    payment_type = models.CharField(max_length=100)
    order_id = models.CharField(max_length=100)
    payment_id = models.CharField(max_length=100)
    payment_amount = models.FloatField()
    address = models.CharField(max_length=100)

    
