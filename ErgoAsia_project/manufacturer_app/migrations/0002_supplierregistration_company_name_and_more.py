# Generated by Django 4.1.13 on 2024-06-16 12:40

from django.db import migrations, models
# Generated by Django 4.1.13 on 2024-06-25 04:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('manufacturer_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='supplierregistration',
            name='company_name',
            field=models.CharField(default=12, max_length=100),
            field=models.CharField(default='Unknown', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='supplierregistration',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=1),
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
