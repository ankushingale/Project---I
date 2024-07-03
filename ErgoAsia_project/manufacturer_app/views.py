from django.shortcuts import render
from .models import SupplierRegistration
from customer_app.models import FinalRequirement
from django.views.decorators.csrf import csrf_exempt
import random  # Assuming Customerdata model is defined in customer_app.models

def manufacturerhome(request):
    # Retrieve the current logged-in supplier based on session or other authentication method
    supplier_id = request.session.get('supplier_id')  # Retrieve supplier_id from session
    if supplier_id:
        try:
            # Retrieve supplier and its category
            supplier = SupplierRegistration.objects.get(supplier_id=supplier_id)
            supplier_category = supplier.supplier_category
            
            # Fetch final requirements matching the supplier's category
            matching_requirements = FinalRequirement.objects.filter(meal_preference=supplier_category)
            
            context = {
                'matching_requirements': matching_requirements
            }
            return render(request, 'manufacturer_app/index.html', context)
        except SupplierRegistration.DoesNotExist:
            # Handle case where supplier_id is not found
            pass
    
    # Redirect or handle cases where supplier_id is not found or session is not valid
    return render(request, 'manufacturer_app/index.html', {'matching_requirements': []})



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
        supplier_category=request.POST.get('category')
       
        supplier_id=random.randint(1000, 9999)

        data=SupplierRegistration(supplier_id=supplier_id,full_name=full_name,company_name=company_name,contact_no=contact,email=email,password=password,address=address,supplier_category=supplier_category)

        data.save()

        message="Registration Done Sucessfully"
        
        return render(request,'manufacturer_app/register.html',{'msg':message})
    return render(request,'manufacturer_app/register.html')


@csrf_exempt
def suppliersignin(request):
    msg_valid=None
    msg_invalid=None
    if request.method=="POST":
        email=request.POST.get('email')
        password=request.POST.get('pass')
        
        request.session['email'] = email

        data=SupplierRegistration.objects.filter(email=email,password=password)

        if data.count()>0:
            msg_valid="Authentication Successfull.....you will redirected to dashboard soon"
        else:
            msg_invalid="Invalid username and password"

        return render(request,'manufacturer_app/login.html',{'msg_valid':msg_valid,'msg_invalid':msg_invalid})

    return render(request,'manufacturer_app/login.html')

def displaySuppliers(request):

    data=SupplierRegistration.objects.all()

def error404V(request):
    # Your view logic here
    return render(request, 'manufacturer_app/error-404.html')

def basic_elements(request):
    # Your view logic here
    return render(request, 'manufacturer_app/basic_elements.html')

def basic_table(request):
    # Your view logic here
    return render(request, 'manufacturer_app/basic-table.html')

# def login(request):
#     # Your view logic here
#     return render(request, 'manufacturer_app/login.html')

# def register(request):
#     # Your view logic here
#     return render(request, 'manufacturer_app/register.html')

# def signinV(request):
#     # Your view logic here
#     return render(request, 'manufacturer_app/sign-in.html')

# def signupV(request):
#     # Your view logic here
#     return render(request, 'manufacturer_app/signup.html')


    