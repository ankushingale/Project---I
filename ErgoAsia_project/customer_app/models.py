from django.db import models

class Customerdata(models.Model):
    customer_id = models.IntegerField(primary_key=True, unique=True, default=123)
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phno = models.CharField(max_length=25)
    password = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    

    def __str__(self):
        return self.name
class Customerrequirements(models.Model):
    customer = models.ForeignKey(Customerdata, on_delete=models.CASCADE)
    # phone_no =models.CharField(max_length=50, unique=True)
    meal_preference = models.CharField(max_length=50)
    Part_Name = models.CharField(max_length=50)
    blank_name = models.CharField(max_length=50)
    draft = models.CharField(max_length=60)
    cname=models.CharField(max_length=50)
    pname=models.CharField(max_length=50)
    cpno=models.CharField(max_length=50)
    desc=models.CharField(max_length=50)
    pr=models.CharField(max_length=50)
    av=models.IntegerField(default=123)
    qs=models.DateField()
    tv=models.IntegerField()
    sop=models.DateField()
    def __str__(self):
        return f"{self.customer.name} - {self.phone_no}"