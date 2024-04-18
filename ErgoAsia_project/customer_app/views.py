from django.shortcuts import render,redirect,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from customer_app.models import *
import random
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required

# from django.conf import settings.
# from django.conf.urls.static import static.
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
        
        return render(request,'customer_app/signup1.html',{'msg':message})

    return render(request,'customer_app/signup1.html')

@csrf_exempt
def customersignin(request):
    msg_valid=None
    msg_invalid=None
    if request.method=="POST":
        email=request.POST.get('email')
        password=request.POST.get('password')

        # Ensure login is called upon successful authentication

        request.session['customer_email'] = email
        
        data=Customerdata.objects.filter(email=email,password=password)
       
        if data.count()>0:
            msg_valid="Authentication Successfull.....you will redirected to home page soon"            # user.save()
            # user=authenticate(request,email=email,password=password)
            # if user is not None:
            #     login(request,user)
            return redirect('customerdashboard')

        else:
            msg_invalid="Invalid username and password"
            # return redirect('customersignin')
        return render(request,'customer_app/signinnew.html',{'msg_valid':msg_valid,'msg_invalid':msg_invalid})

    return render(request,'customer_app/signinnew.html')

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
        pdf_file=request.FILES.get('pdf_file')
        company_name=request.POST.get('cname')
        project_name=request.POST.get('pname')
        part_no=request.POST.get('cpno')
        description=request.POST.get('desc')
        Part_revision=request.POST.get('pr')
        Anual_volume=request.POST.get('av')
        Quote_submission=request.POST.get('qs')
        target_value=request.POST.get('tv')
        start_of_production=request.POST.get('sop')
        
        # def upload_pdf(request):
        #     if request.method == 'POST':
        #         pdf_file = request.FILES.get('pdf_file')
        #         if pdf_file:
        #             with open('media/' + pdf_file.name, 'wb') as f:
        #                 for chunk in pdf_file.chunks():
        #                     f.write(chunk)
        #         return HttpResponse('File uploaded successfully!')
        #     else:
        #         return HttpResponse('No file uploaded!')

        # upload_pdf(request)

        data=Customerrequirements(meal_preference=meal_preference,Part_Name=Part_Name,blank_name=blank_name,upload_file=pdf_file,cname=company_name,pname=project_name,cpno=part_no,desc=description,pr=Part_revision,av=Anual_volume,qs=Quote_submission,tv=target_value,sop=start_of_production,customer=Customerdata.objects.get(customer_id = cid))
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

    return render(request, 'customer_app/requirementsform.html', {'customer_data': customer_data})

# def customersign(request):
#     return render(request,'customer_app/signinnew.html')
#     # return render(request,'customer_app/profile.html')
#     # return render(request,'customer_app/index.html')

def customerdashboard(request):
    return render(request,'customer_app/dashboard1.html')

def customertables(request):
    return render(request,'customer_app/tables.html')
