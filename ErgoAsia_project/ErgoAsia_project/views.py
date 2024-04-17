from django.shortcuts import render

def hometemplate(request):
    # request.session['customer_email'] = None
    return render(request,'Templates/home.html')