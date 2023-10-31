from django.shortcuts import render

# Create your views here.
def customerhome(request):
    return render(request,'customer home.html')