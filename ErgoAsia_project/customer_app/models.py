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

   
