from distutils.command.upload import upload
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Customer(models.Model):
    cust_name = models.CharField(max_length=40)
    cust_email = models.CharField(max_length=50)
    cust_phone = models.BigIntegerField()
    cust_image = models.ImageField(upload_to='customer/')
    cust_password = models.CharField(max_length=20)



class Seller(models.Model):
    seller_name = models.CharField(max_length=40)
    seller_email = models.CharField(max_length=50)
    seller_adds = models.CharField(max_length=100)
    seller_phone = models.BigIntegerField()
    seller_accno = models.BigIntegerField()
    seller_ifsc = models.CharField(max_length=30)
    seller_image = models.ImageField(upload_to='seller/')
    seller_password = models.CharField(max_length=20)


class Admin(models.Model):
    admin_id = models.IntegerField()
    admin_password = models.CharField(max_length=20)
    






