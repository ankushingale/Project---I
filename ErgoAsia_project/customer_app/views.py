from django.shortcuts import get_object_or_404, render,redirect,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from customer_app.models import *
import random
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from .models import Customerrequirements
from .models import FinalRequirement, Customerdata
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime
# customer_app/views.py
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


# from django.conf import settings.
# from django.conf.urls.static import static.
# Create your views here.

def customerhome(request):
    return render(request,'customer_app/home.html')
@csrf_exempt

# def customersignup(request):
#     message=Nonegit 
#     if request.method=="POST":
#         fname=request.POST.get('fname')
#         lname=request.POST.get('lname')
#         email=request.POST.get('email')
#         phno=request.POST.get('phno')
#         password=request.POST.get('password')
#         address=request.POST.get('addr')
#         name = f"{fname} {lname}"

#         customer_id=random.randint(1000, 9999)

#         data=Customerdata(customer_id=customer_id,name=name,email=email,phno=phno,password=password,address=address)
#         data.save()
               
#         message="Registration Done Sucessfully"
        
#         return render(request,'customer_app/signup1.html',{'msg':message})

#     return render(request,'customer_app/signup1.html')

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
        
    return render(request, 'customer_app/signup1.html', {'msg': message})

@csrf_exempt
def customersignin(request):
    msg_valid = None
    msg_invalid = None
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        request.session['customer_email'] = email
        data = Customerdata.objects.filter(email=email, password=password)
       
        if data.count() > 0:
            msg_valid = "Authentication Successful... you will be redirected to the home page soon"
            data_values = data.first()
            request.session['customer_id'] = data_values.customer_id
            data_values.is_logged_in = True  # Set is_logged_in to True
            data_values.save()

            return redirect('Cdashboard')
        else:
            msg_invalid = "Invalid username and password"
        
        return render(request, 'customer_app/signinnew.html', {'msg_valid': msg_valid, 'msg_invalid': msg_invalid})

    return render(request, 'customer_app/signinnew.html')


def customerrequirements(request):
    if request.method == "POST":
        cid = request.POST.get('cid')
        if not cid:
            return HttpResponse("Customer ID is missing.", status=400)

        meal_preference = request.POST.get('meal_preference')
        Part_Name = request.POST.get('Part_Name')
        blank_name = request.POST.get('blank_name')
        pdf_file = request.FILES.get('pdf_file')
        company_name = request.POST.get('cname')
        project_name = request.POST.get('pname')
        part_no = request.POST.get('cpno')
        description = request.POST.get('desc')
        Part_revision = request.POST.get('pr')
        Anual_volume = request.POST.get('av')
        Quote_submission = request.POST.get('qs')
        target_value = request.POST.get('tv')
        start_of_production = request.POST.get('sop')
        working_status = request.POST.get('working_status')

        project_id = random.randint(1000, 9999)

        try:
            customer = Customerdata.objects.get(customer_id=cid)
        except Customerdata.DoesNotExist:
            return HttpResponse("Customer not found.", status=404)

        data = Customerrequirements(
            project_id=project_id,
            meal_preference=meal_preference,
            Part_Name=Part_Name,
            blank_name=blank_name,
            upload_file=pdf_file,
            cname=company_name,
            pname=project_name,
            cpno=part_no,
            desc=description,
            pr=Part_revision,
            av=Anual_volume,
            qs=Quote_submission,
            tv=target_value,
            sop=start_of_production,
            working_status=working_status,
            customer=customer
        )
        data.save()
        return redirect('customer-tables')

    customer_email = request.session.get('customer_email', None)
    customer_data = Customerdata.objects.filter(email=customer_email)

    for customer in customer_data:
        names = customer.name.split(" ", 1)
        first_name = names[0]
        last_name = names[1] if len(names) > 1 else ""

        print("Customer ID:", customer.customer_id)
        print("First Name:", first_name)
        print("Last Name:", last_name)
        print("Email:", customer.email)

    return render(request, 'customer_app/tablescopy.html', {'customer_data': customer_data})

# def customersign(request):
#     return render(request,'customer_app/signinnew.html')
#     # return render(request,'customer_app/profile.html')
#     # return render(request,'customer_app/index.html')

from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Customerrequirements

def customerdashboard(request):
    # Retrieve customer ID from session
    customer_id = request.session.get('customer_id')

    # Initialize context dictionary
    context = {}

    if customer_id:
        # Query to retrieve customer data
        customer_data = Customerrequirements.objects.filter(customer_id=customer_id)
        FinalRequirement_data = FinalRequirement.objects.filter(customer_id=customer_id)
        customer_profil_data = Customerdata.objects.filter(customer_id=customer_id)

        # Count total orders for the customer
        total_orders = FinalRequirement_data.filter(approval_status='approved').count()
        

        # Count completed orders
        completed_orders = customer_data.filter(working_status='completed').count()

        # Count pending orders
        pending_orders = customer_data.filter(working_status='pending').count()

        # Calculate new orders received today
        # today = datetime.now().date()
        new_order = customer_data.all().count()

        # Count working orders
        working_orders = FinalRequirement_data.filter(working_status='working').count()
    

        # Update context with customer_data and counts
        context.update({
            'final_cdata' : FinalRequirement_data,
            'cdata': customer_data,
            'total_orders': total_orders,
            'completed_orders': completed_orders,
            'pending_orders': pending_orders,
            'working_orders': working_orders,
            'customer_profil_data':customer_profil_data,
            'new_order':new_order,
        })
    else:
        # Handle case where customer_id is not found in session
        return redirect('login')  # Redirect to login page or handle appropriately

    # Render template with updated context
    return render(request, 'customer_app/Cdashboard.html', context)


def customertables(request):
    
    customer_id = request.session.get('customer_id', None)

    customer_data=Customerrequirements.objects.filter(customer_id=customer_id)

    return render(request,'customer_app/tables.html',{'cdata':customer_data})

def customerprofile(request):
    return render(request,'customer_app/profile.html')


def displayModel(request,pk):
    customer_data=Customerrequirements.objects.filter(customer_id=pk)
    
    return render(request,'customer_app/editmodel.html',{'customer_data':customer_data})

# views.py

def categorymodel(request, customer_id, category):
    try:
        customer_data = FinalRequirement.objects.filter(customer_id=customer_id, meal_preference=category)
        return render(request, 'customer_app/customer_caategoory_modee.html', {'customer_data': customer_data})
    except FinalRequirement.DoesNotExist:
        return render(request, 'customer_app/customer_caategoory_modee.html', {'customer_data': None})


def edit_customer_requirement(request, project_id):
    requirement = get_object_or_404(Customerrequirements, project_id=project_id)

    if request.method == "POST":
        # Extract all fields from POST data
        meal_preference = request.POST.get('meal_preference')
        part_name = request.POST.get('Part_Name')
        blank_name = request.POST.get('blank_name')
        pdf_file = request.FILES.get('pdf_file')
        company_name = request.POST.get('cname')
        project_name = request.POST.get('pname')
        part_no = request.POST.get('cpno')
        description = request.POST.get('desc')
        part_revision = request.POST.get('pr')
        annual_volume = request.POST.get('av')
        quote_submission = request.POST.get('qs')
        target_value = request.POST.get('tv')
        start_of_production = request.POST.get('sop')
        working_status = request.POST.get('status')  # Get the status value

        # Update the requirement object with new values
        requirement.meal_preference = meal_preference
        requirement.Part_Name = part_name
        requirement.blank_name = blank_name
        if pdf_file:
            requirement.upload_file = pdf_file
        requirement.cname = company_name
        requirement.pname = project_name
        requirement.cpno = part_no
        requirement.desc = description
        requirement.pr = part_revision
        requirement.av = annual_volume
        requirement.qs = quote_submission
        requirement.tv = target_value
        requirement.sop = start_of_production
        requirement.working_status = working_status  # Update the status field
        requirement.save()  # Save the updated requirement object

        return redirect('customer-tables')  # Redirect to Cdashboard URL after saving

    # If request method is GET, render the edit form with current requirement data
    return render(request, 'customer_app/edit_requirement.html', {'requirement': requirement})

def delete_customer_requirement(request, project_id):
    customer_requirement = get_object_or_404(Customerrequirements, project_id=project_id)

    if request.method == "POST":
        customer_requirement.delete()
        # Notify admin or log the deletion here
        return redirect('customer-tables')

    return render(request, 'customer_app/delete_requirement.html', {'requirement': customer_requirement})


def categorymodel(request, customer_id, category):
    try:
        customer_data = Customerrequirements.objects.filter(customer_id=customer_id, meal_preference=category)
        return render(request, 'customer_app/customer_caategoory_modee.html', {'customer_data': customer_data})
    except Customerrequirements.DoesNotExist:
        return render(request, 'customer_app/customer_caategoory_modee.html', {'customer_data': None})

def customer_final_requirements(request):
    try:
        # Retrieve customer ID from the session
        customer_id = request.session.get('customer_id')
        
        if not customer_id:
            # Handle case where customer ID is not in session
            return redirect('customersignin')
        
        # Fetch all requirements for the logged-in customer
        final_requirements = FinalRequirement.objects.all()

        print(f"Customer ID: {customer_id}")  # Debug output
        print(f"Final Requirements Query: {final_requirements.query}")  # Debug output

        return render(request, 'customer_app/dashboard.html', {'final_requirements': final_requirements})
    except Exception as e:
        print(f"Error fetching final requirements: {str(e)}")
        return render(request, 'customer_app/dashboard.html', {'final_requirements': None})
    

def custom_logout(request):
    customer_id = request.session.get('customer_id')
    if customer_id:
        customer = Customerdata.objects.get(customer_id=customer_id)
        customer.is_logged_in = False
        customer.save()
    logout(request)
    # Redirect to a different path after logout
    return redirect('/customer-sign') 


def final_requirement_list(request, status=None):
    if status:
        final_requirements = FinalRequirement.objects.filter(working_status=status)
    else:
        final_requirements = FinalRequirement.objects.all()
    return render(request, 'customer_app/filtered_requirements.html', {'final_requirements': final_requirements})
