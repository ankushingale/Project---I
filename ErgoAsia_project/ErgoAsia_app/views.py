from datetime import timezone
from django.contrib import messages
import random
from django.shortcuts import render, redirect, get_object_or_404
from customer_app.models import Customerdata, Customerrequirements, FinalRequirement
from manufacturer_app.models import SupplierRegistration
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime

from django.http import JsonResponse

# Create your views here.

def home(request):
    return render(request, 'home.html')

def ErgoAsiahome(request):
    return render(request, 'ErgoAsia_app/home.html')

def dashboard(request):
    
    today_date = datetime.now().date()
    formatted_today = today_date.strftime("%Y-%m-%d")
    print(formatted_today)
    data=Customerrequirements.objects.filter(request_date=formatted_today)
    count = Customerrequirements.objects.count()
    total_coustomer=Customerdata.objects.count()
    supplier_count=SupplierRegistration.objects.count()
    

    # new_supplier_count = new_suppliers.count()
    return render(request,'ErgoAsia_app/dashboard.html',{'req':data,'cnt':count,'total_coustomer' :total_coustomer,'supplier_count':supplier_count,'todays_date': today_date})
    # Querying all customer requirements
    approved_projects = FinalRequirement.objects.filter(approval_status='approved')
    data = Customerrequirements.objects.all()
    count = Customerrequirements.objects.count()
    total_customer = Customerdata.objects.count()
    supplier_count = SupplierRegistration.objects.count()
    supplier = SupplierRegistration.objects.all()

    return render(request, 'ErgoAsia_app/dashboard.html', {
        'approved_projects': approved_projects,
        'req': data,
        'cnt': count,
        'total_customer': total_customer,
        'supplier_count': supplier_count,
        'supplier':supplier
    })

def supplier(request):
    return render(request, 'ErgoAsia_app/supplier.html')

def notifications(request):
    customer_data = Customerrequirements.objects.all()
    supplier_data = SupplierRegistration.objects.all()

    return render(request, 'ErgoAsia_app/notifications.html', {
        'customer_data': customer_data,
        'supplier_data': supplier_data
    })

def registrationtable(request):
    customer_data = Customerdata.objects.all()
    supplier_data = SupplierRegistration.objects.all()
    return render(request, 'ErgoAsia_app/tables.html', {
        'customer_data': customer_data,
        'supplier_data': supplier_data
    })

@csrf_exempt
def ergoasiasignin(request):
    msg_valid = None
    msg_invalid = None
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')

        if username == "Admin" and password == "Admin":
            msg_valid = "Authentication Successfull.....you will be redirected to the dashboard page soon"
        else:
            msg_invalid = "Invalid username and password"

        return render(request, 'ErgoAsia_app/sign-in.html', {
            'msg_valid': msg_valid,
            'msg_invalid': msg_invalid
        })

    return render(request, 'ErgoAsia_app/sign-in.html')


def DisplayModel(request, pk):
    customer_data = Customerrequirements.objects.filter(customer_id=pk)
    
    return render(request, 'ErgoAsia_app/editmodel.html', {
        'customer_data': customer_data
    })


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


def supplierregistration(request):
    message = None
    if request.method == "POST":
        full_name = request.POST.get('fullname')
        contact = request.POST.get('cno')
        email = request.POST.get('email')
        password = request.POST.get('pass')
        address = request.POST.get('addr')
        company_name = request.POST.get('company')
        supplier_category = request.POST.get('category')

        supplier_id = random.randint(1000, 9999)

        data = SupplierRegistration(
            supplier_id=supplier_id,
            full_name=full_name,
            contact_no=contact,
            email=email,
            password=password,
            address=address,
            company_name=company_name,
            supplier_category=supplier_category
        )

        data.save()

        message = "Registration Done Successfully"

        return render(request, 'ErgoAsia_app/new_supplier.html', {'msg': message})

    return render(request, 'ErgoAsia_app/new_supplier.html')


def edit_supplier(request, supplier_id):
    supplier = get_object_or_404(SupplierRegistration, supplier_id=supplier_id)
    if request.method == 'POST':
        supplier.full_name = request.POST.get('fullname')
        supplier.contact_no = request.POST.get('cno')
        supplier.email = request.POST.get('email')
        supplier.password = request.POST.get('pass')
        supplier.address = request.POST.get('addr')
        supplier.company_name = request.POST.get('company')
        supplier.supplier_category = request.POST.get('category')
        supplier.save()
        return redirect('registrationtable')  # Adjust this to your actual supplier list view name

    return render(request, 'ErgoAsia_app/edit_supplier.html', {'supplier': supplier})


def delete_supplier(request, supplier_id):
    supplier = get_object_or_404(SupplierRegistration, supplier_id=supplier_id)
    if request.method == 'POST':
        supplier.delete()
        return redirect('registrationtable')  # Adjust this to your actual supplier list view name

    return render(request, 'ErgoAsia_app/confirm_delete.html', {'supplier': supplier})


def supplier_list(request):
    suppliers = SupplierRegistration.objects.all()
    supplier_count = suppliers.count()
    return render(request, 'ErgoAsia_app/dashboard.html', {'suppliers': suppliers, 'supplier_count': supplier_count})


def customer_detail(request, customer_id):
    customer = get_object_or_404(Customerdata, customer_id=customer_id)
    customer_requirements = Customerrequirements.objects.filter(customer_id=customer_id)
    customer_requirements_final = FinalRequirement.objects.filter(customer_id=customer_id)

    context = {
        'customer': customer,
        'customer_requirements': customer_requirements,
        'customer_requirements_final': customer_requirements_final,
    }

    return render(request, 'ErgoAsia_app/customer_detail.html', context)


def project_details(request, customer_id, project_id):
    customer = get_object_or_404(Customerdata, pk=customer_id)
    project = get_object_or_404(Customerrequirements, pk=project_id, customer=customer)

    if request.method == 'POST' and 'approve' in request.POST and request.POST['approve'] == 'yes':
        # Create a FinalRequirement entry
        FinalRequirement.objects.create(
            project_id=project.project_id,
            customer=project.customer,
            meal_preference=project.meal_preference,
            Part_Name=project.Part_Name,
            blank_name=project.blank_name,
            upload_file=project.upload_file,
            cname=project.cname,
            pname=project.pname,
            cpno=project.cpno,
            desc=project.desc,
            pr=project.pr,
            av=project.av,
            qs=project.qs,
            tv=project.tv,
            sop=project.sop,
            working_status=project.working_status,
            approval_status='approved'  # Set the approval status to 'approved'
        )
        # Delete the project from Customerrequirements
        project.delete()

        return redirect('registrationtable')  # Redirect after processing
    
    return render(request, 'ErgoAsia_app/project_details.html', {
        'customer': customer,
        'project': project
    })



    
    

def final_project_details(request, project_id):
    project = get_object_or_404(FinalRequirement, project_id=project_id)
    customer_name = project.customer.name
    customer_id = project.customer.customer_id # Assuming 'customer' is a ForeignKey to Customerdata

    return render(request, 'ErgoAsia_app/final_project_details.html', {
        'project': project,
        'customer_name': customer_name,
        'customer_id' : customer_id
    })

def final_requirements_view(request):
    msg_valid = None
    if request.method == 'POST':
        # customer_id=customer_id.POST.get('customer_id')
        project_id = request.POST.get('project_id')
        working_status = request.POST.get('working_status')
        requirement = get_object_or_404(FinalRequirement, project_id=project_id)
        requirement.working_status = working_status
        requirement.save()
        msg_valid = "succ"
        return redirect('final_requirements_view')  # Redirect back to the same view after update
    
    return render(request, 'ErgoAsia_app/result.html', {'msg_valid': msg_valid})




def supplier_list(request):
    suppliers = SupplierRegistration.objects.all()
    return render(request, 'ErgoAsia_app/dashboard.html', {'suppliers': suppliers})


def supplier_detail(request, supplier_id):
    # Retrieve the supplier using supplier_id
    supplier = get_object_or_404(SupplierRegistration, supplier_id=supplier_id)  # Fetch the supplier

    # Fetch approved orders where the category matches the supplier's category
    approved_orders = FinalRequirement.objects.filter(
        approval_status='approved',
        meal_preference=supplier.supplier_category  # Use the correct field for category
    )

    return render(request, 'ErgoAsia_app/supplier_detail.html', {
        'supplier': supplier,
        'approved_orders': approved_orders,
    })