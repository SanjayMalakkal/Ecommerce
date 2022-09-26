from distutils.command.upload import upload
from django.db import models

# Create your models here.

class Customer(models.Model):
    cust_name = models.CharField(max_length=40)
    cust_email = models.CharField(max_length=50)
    cust_phone = models.BigIntegerField()
    cust_image = models.ImageField(upload_to='customer/')
    cust_password = models.CharField(max_length=20)



class Seller(models.Model):
    sell_name = models.CharField(max_length=40)
    sell_email = models.CharField(max_length=50)
    sell_phone = models.BigIntegerField()
    sell_image = models.ImageField(upload_to='seller/')
    sell_password = models.CharField(max_length=20)


class Admin(models.Model):
    admin_id = models.IntegerField()
    admin_password = models.CharField(max_length=20)
    






