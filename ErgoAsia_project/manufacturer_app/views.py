from django.shortcuts import render

# Create your views here.
def manufacturerhome(request):
    return render(request,'manufacturer_app/home.html')