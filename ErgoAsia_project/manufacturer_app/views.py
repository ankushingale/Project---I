from django.shortcuts import render
import random
from manufacturer_app.models import SupplierRegistration
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def manufacturerhome(request):
    return render(request,'manufacturer_app/home.html')

@csrf_exempt
def supplierregistration(request):
    message=None
    if request.method=="POST":
        full_name=request.POST.get('fullname')
        company_name=request.POST.get('cname')
        contact=request.POST.get('cno')
        email=request.POST.get('email')
        password=request.POST.get('pass')
        address = request.POST.get('addr')

        supplier_id=random.randint(1000, 9999)

        data=SupplierRegistration(supplier_id=supplier_id,full_name=full_name,company_name=company_name,contact_no=contact,email=email,password=password,address=address)

        data.save()

        message="Registration Done Sucessfully"
        
        return render(request,'manufacturer_app/signup.html',{'msg':message})
    return render(request,'manufacturer_app/signup.html')


@csrf_exempt
def suppliersignin(request):
    msg_valid=None
    msg_invalid=None
    if request.method=="POST":
        email=request.POST.get('email')
        password=request.POST.get('password')

        data=SupplierRegistration.objects.filter(email=email,password=password)

        if data.count()>0:
            msg_valid="Authentication Successfull.....you will redirected to home page soon"
        else:
            msg_invalid="Invalid username and password"

        return render(request,'manufacturer_app/sign-in.html',{'msg_valid':msg_valid,'msg_invalid':msg_invalid})

    return render(request,'manufacturer_app/sign-in.html')

def displaySuppliers(request):

    data=SupplierRegistration.objects.all()

    