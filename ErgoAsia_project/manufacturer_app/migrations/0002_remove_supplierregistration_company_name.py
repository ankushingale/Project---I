# Generated by Django 4.1.13 on 2024-05-10 16:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manufacturer_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='supplierregistration',
            name='company_name',
        ),
    ]
