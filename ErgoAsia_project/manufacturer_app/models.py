from django.db import models

# Create your models here.
class SupplierRegistration(models.Model):
    supplier_id=models.IntegerField(primary_key=True, unique=True,default=123)
    full_name=models.CharField(max_length=50)
    company_name=models.CharField(max_length=50)
    contact_no=models.CharField(max_length=50)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    supplier_category=models.CharField(max_length=100)

    def __str__(self):
        return self.full_name
