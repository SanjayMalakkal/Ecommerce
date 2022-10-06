from django.db import models

from common.models import Customer, Seller
from seller.models import Product

# Create your models here.

class Cart(models.Model):
    customer = models.ForeignKey(Customer,on_delete = models.CASCADE)
    product = models.ForeignKey(Product,on_delete = models.CASCADE)