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