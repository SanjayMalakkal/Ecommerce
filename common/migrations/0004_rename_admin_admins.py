# Generated by Django 4.1.1 on 2022-09-30 16:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0003_alter_admin_admin_id'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Admin',
            new_name='Admins',
        ),
    ]