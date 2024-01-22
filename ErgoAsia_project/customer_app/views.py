from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from customer_app.models import *
import random
from django.contrib.auth.decorators import login_required

# Create your views here.
def customerhome(request):
    return render(request,'customer_app/home.html')
@csrf_exempt
def customersignup(request):
    message=None
    if request.method=="POST":
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        email=request.POST.get('email')
        phno=request.POST.get('phno')
        password=request.POST.get('password')
        address=request.POST.get('addr')
        name = f"{fname} {lname}"

        customer_id=random.randint(1000, 9999)

        data=Customerdata(customer_id=customer_id,name=name,email=email,phno=phno,password=password,address=address)

        data.save()

        message="Registration Done Sucessfully"
        
        return render(request,'customer_app/signup.html',{'msg':message})

    return render(request,'customer_app/signup.html')

@csrf_exempt
def customersignin(request):
    msg_valid=None
    msg_invalid=None
    if request.method=="POST":
        email=request.POST.get('email')
        password=request.POST.get('password')
        
        request.session['customer_email'] = email

        data=Customerdata.objects.filter(email=email,password=password)

        if data.count()>0:
            msg_valid="Authentication Successfull.....you will redirected to home page soon"
        else:
            msg_invalid="Invalid username and password"

        return render(request,'customer_app/sign-in.html',{'msg_valid':msg_valid,'msg_invalid':msg_invalid})

    return render(request,'customer_app/sign-in.html')

@csrf_exempt
# @login_required
def customerrequirements(request):
    if request.method=="POST":

        # first_name=request.POST.get('first_name')
        # last_name=request.POST.get('last_name')
        cid=request.POST.get('cid')
        # email=request.POST.get('email')
        # phone_no=request.POST.get('phone_number')
        meal_preference=request.POST.get('meal_preference')
        Part_Name=request.POST.get('Part_Name')
        blank_name=request.POST.get('blank_name')
        draft=request.POST.get('payable')


        data=Customerrequirements(meal_preference=meal_preference,Part_Name=Part_Name,blank_name=blank_name,draft=draft,customer=Customerdata.objects.get(customer_id = cid))
        data.save()
        
    customer_email = request.session.get('customer_email', None)
    customer_data=Customerdata.objects.filter(email=customer_email)

    for customer in customer_data:
        names = customer.name.split(" ", 1)
        first_name = names[0]
        last_name = names[1] if len(names) > 1 else ""

        print("Customer ID:", customer.customer_id)
        print("First Name:", first_name)
        print("Last Name:", last_name)
        print("Email:", customer.email)

    return render(request, 'customer_app/requirementsform.html', {'customer_data': customer_data, 'first_name': first_name, 'last_name': last_name})
