"""
URL configuration for ErgoAsia_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from manufacturer_app import views

urlpatterns = [
    path('manufacturerhome',views.manufacturerhome,name="manufacturerhome"),
    path('supplier-registration',views.supplierregistration,name="supplierregistration"),
    path('supplier-signin',views.suppliersignin,name="suppliersignin"),
    path('error404', views.error404V, name='error404N'),
    path('basic_elements', views.basic_elements, name='basic_elementsN'),
    path('basic_table', views.basic_table, name='basic_tableN'),
    path('supplierlogin', views.login, name='loginN'),
    path('supplierregister', views.register, name='registerN'),
    # path('signin/', views.login, name='signinN'),
    # path('signup/', views.signup, name='signupN'),
    

]
