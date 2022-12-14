# Generated by Django 4.1.1 on 2022-10-01 07:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('common', '0005_admin_delete_admins_remove_customer_cust_adds'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_name', models.CharField(max_length=20)),
                ('p_number', models.IntegerField()),
                ('p_description', models.CharField(max_length=30)),
                ('p_price', models.BigIntegerField()),
                ('p_stock', models.IntegerField()),
                ('p_image', models.ImageField(upload_to='products/')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.seller')),
            ],
        ),
    ]
