# Generated by Django 4.1.1 on 2022-10-18 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0005_admin_delete_admins_remove_customer_cust_adds'),
    ]

    operations = [
        migrations.AddField(
            model_name='seller',
            name='seller_status',
            field=models.CharField(default='pending', max_length=40),
        ),
    ]
