# Generated by Django 4.1.1 on 2022-09-30 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_customer_cust_adds'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin',
            name='admin_id',
            field=models.CharField(max_length=30),
        ),
    ]
