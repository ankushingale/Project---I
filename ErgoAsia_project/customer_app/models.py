from django.db import models

# Create your models here.
class Customer(models.Model):
    customer_id=models.IntegerField(primary_key=True, unique=True,default=123)
    name=models.CharField(max_length=50)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=50)
    address=models.CharField(max_length=100)

    # id = models.BigAutoField(customer_id,primary_key=True)

    def __str__(self):
        return self.name
    
class Customerrequirements(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    company=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    phone_no=models.CharField(max_length=50)
    meal_preference=models.CharField(max_length=50)
    Part_Name=models.CharField(max_length=50)
    blank_name=models.CharField(max_length=50)
    draft=models.CharField(max_length=50)

   
