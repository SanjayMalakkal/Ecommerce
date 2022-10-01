from distutils.command.upload import upload
from ftplib import MAXLINE
from django.db import models
from common.models import Seller

# Create your models here.

class Product(models.Model):
    seller = models.ForeignKey(Seller,on_delete=models.CASCADE)
    p_name = models.CharField(max_length = 20)
    p_number = models.IntegerField()
    p_description = models.CharField(max_length = 30)
    p_price = models.BigIntegerField()
    p_stock = models.IntegerField()
    p_image = models.ImageField(upload_to = 'products/')
    
