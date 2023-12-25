from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from customer_app.models import Customer
import random
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
        password=request.POST.get('password')
        address=request.POST.get('addr')
        name = f"{fname} {lname}"

        customer_id=random.randint(1000, 9999)

        data=Customer(customer_id=customer_id,name=name,email=email,password=password,address=address)

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

        data=Customer.objects.filter(email=email,password=password)

        if data.count()>0:
            msg_valid="Authentication Successfull.....you will redirected to home page soon"
        else:
            msg_invalid="Invalid username and password"

        return render(request,'customer_app/sign-in.html',{'msg_valid':msg_valid,'msg_invalid':msg_invalid})

    return render(request,'customer_app/sign-in.html')
