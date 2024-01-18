from django.shortcuts import render
from customer_app.models import Customerdata
from manufacturer_app.models import SupplierRegistration
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def home(request):
    return render(request,'home.html')

def ErgoAsiahome(request):
    return render(request,'ErgoAsia_app/home.html')

def dashboard(request):
    return render(request,'ErgoAsia_app/dashboard.html')

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



