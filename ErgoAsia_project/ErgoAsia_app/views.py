from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'home.html')

def ErgoAsiahome(request):
    return render(request,'ErgoAsia_app/home.html')

def dashboard(request):
    return render(request,'ErgoAsia_app/dashboard.html')

def registrationtable(request):
    return render(request,"ErgoAsia_app/tables.html")

