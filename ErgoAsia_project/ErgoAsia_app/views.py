import random
from django.shortcuts import render, redirect, get_object_or_404
from customer_app.models import Customerdata,Customerrequirements
from manufacturer_app.models import SupplierRegistration
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def home(request):
    return render(request,'home.html')

def ErgoAsiahome(request):
    return render(request,'ErgoAsia_app/home.html')

def dashboard(request):

    data=Customerrequirements.objects.all()
    count = Customerrequirements.objects.count()
    total_coustomer=Customerdata.objects.count()

    return render(request,'ErgoAsia_app/dashboard.html',{'req':data,'cnt':count,'total_coustomer' :total_coustomer})

def supplier(request):
    return render(request,'ErgoAsia_app/supplier.html')

def notifications(request):
    return render(request,'ErgoAsia_app/notifications.html')

def registrationtable(request):
    customer_data=Customerdata.objects.all()
    supplier_data=SupplierRegistration.objects.all()
    return render(request,'ErgoAsia_app/tables.html',{'customer_data':customer_data,'supplier_data':supplier_data})

@csrf_exempt
def ergoasiasignin(request):
    msg_valid=None
    msg_invalid=None
    if request.method=='POST':

        username=request.POST.get('uname')
        password=request.POST.get('pass')

        if username=="Admin" and password=="Admin":
            msg_valid="Authentication Successfull.....you will redirected to dashboard page soon"
        else:
            msg_invalid="Invalid username and password"

        return render(request,'ErgoAsia_app/sign-in.html',{'msg_valid':msg_valid,'msg_invalid':msg_invalid})

        
    return render(request,'ErgoAsia_app/sign-in.html')


def DisplayModel(request,pk):

    customer_data=Customerrequirements.objects.filter(customer_id=pk)
    
    return render(request,'ErgoAsia_app/editmodel.html',{'customer_data':customer_data})

def sortby(request):
    print('inside sortby')
    if request.method == 'POST':
        category = request.POST.get('category')  # Retrieve the 'category' value from POST data
        customer_requirements_data = Customerrequirements.objects.filter(meal_preference=category)

        print("hello")
        for requirement in customer_requirements_data:
            print(requirement.first.pname)
        
            
def edit_customer(request, customer_id):
    customer = get_object_or_404(Customerdata, customer_id=customer_id)
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phno = request.POST.get('phno')
        address = request.POST.get('address')
        
        customer.name = name
        customer.email = email
        customer.phno = phno
        customer.address = address
        customer.save()
        
        return redirect('registrationtable')  # Redirect to dashboard after saving
    
    return render(request, 'ErgoAsia_app/edit_customer.html', {'customer': customer})

@csrf_exempt
def delete_customer(request, customer_id):
    customer = get_object_or_404(Customerdata, customer_id=customer_id)
    if request.method == "POST":
        customer.delete()
        return redirect('registrationtable')
    return render(request, 'ErgoAsia_app/delete_confirm.html', {'customer': customer})


def customersignup(request):
    message = None
    if request.method == "POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        phno = request.POST.get('phno')
        password = request.POST.get('password')
        address = request.POST.get('addr')
        name = f"{fname} {lname}"

        customer_id = random.randint(1000, 9999)

        data = Customerdata(customer_id=customer_id, name=name, email=email, phno=phno, password=password, address=address)
        data.save()
               
        message = "Registration Done Successfully"
        
    return render(request, 'ErgoAsia_app/new_customer.html', {'msg': message})

import random

def supplierregistration(request):
    message = None
    if request.method == "POST":
        full_name = request.POST.get('fullname')
        contact = request.POST.get('cno')
        email = request.POST.get('email')
        password = request.POST.get('pass')
        address = request.POST.get('addr')
        supplier_category = request.POST.get('category')

        supplier_id = random.randint(1000, 9999)

        data = SupplierRegistration(
            supplier_id=supplier_id,
            full_name=full_name,
            contact_no=contact,
            email=email,
            password=password,
            address=address,
            supplier_category=supplier_category
        )

        data.save()

        message = "Registration Done Successfully"

        return render(request, 'ErgoAsia_app/new_supplier.html', {'msg': message})

    return render(request, 'ErgoAsia_app/new_supplier.html')