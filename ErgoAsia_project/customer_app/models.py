from django.db import models
from djongo import models as djongo_models
from django.utils import timezone

class Customerdata(models.Model):
    customer_id = models.IntegerField(primary_key=True, unique=True, default=123)
    name = models.CharField(max_length=50)
    email = models.qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqEmailField(unique=True)
    phno = models.CharField(max_length=25)
    password = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

class PDFFileField(djongo_models.FileField):
    description = "PDF File"

    def __init__(self, *args, **kwargs):
        kwargs['format'] = 'pdf'
        super().__init__(*args, **kwargs)

class Customerrequirements(models.Model):
    STATUS_CHOICES = (
        ('working', 'Working'),
        ('pending', 'Pending'),
        ('completed', 'Completed'),
    )
    project_id = models.IntegerField(primary_key=True)
    customer = models.ForeignKey(Customerdata, on_delete=models.CASCADE)
    meal_preference = models.CharField(max_length=50)
    Part_Name = models.CharField(max_length=50)
    blank_name = models.CharField(max_length=50)
    upload_file = models.FileField(upload_to='uploads/', max_length=250)
    cname=models.CharField  (max_length=50)
    pname=models.CharField(max_length=50)
    cpno=models.CharField(max_length=50)
    desc=models.CharField(max_length=50)
    pr=models.CharField(max_length=50)
    av=models.IntegerField(default=123)
    qs=models.DateField() 
    tv=models.IntegerField()
    sop=models.DateField()
    request_date = models.DateTimeField(auto_now_add=True)
    cname = models.CharField(max_length=50)
    pname = models.CharField(max_length=50)
    cpno = models.CharField(max_length=50)
    desc = models.CharField(max_length=50)
    pr = models.CharField(max_length=50)
    av = models.IntegerField(default=123)
    qs = models.DateField()
    tv = models.IntegerField()
    sop = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='working')

    def __str__(self):
        return f"{self.project_id} - {self.cname}"

