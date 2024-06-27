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
from customer_app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('customerhome',views.customerhome,name="customerhome"),
    path('customer-signup',views.customersignup,name="customersignup"),
    # path('customer-signin',views.customersignin,name="customersignin"),
    path('customer-requirements', views.customerrequirements, name='customer-requirements'),
    path('customer-tables', views.customertables, name='customer-tables'), 
    path('customer-sign',views.customersignin,name="customersign"),
    path('customer-dashboard',views.customerdashboard,name="Cdashboard"),
    # path('customer-tables', views.customertables,name="customertables"),
    path('customer-profile', views.customerprofile,name="customerprofile"),
    path('edit/<int:pk>',views.displayModel,name="customereditmodel"),
    # path('model_category/<int:pk>',views.categorymodel,name="categorymodel"),
    path('model_category/<int:customer_id>/<str:category>/', views.categorymodel, name='model_category'),
    path('edit_requirement/<int:project_id>/', views.edit_customer_requirement, name='edit_customer_requirement'),
    path('delete_requirement/<int:project_id>/', views.delete_customer_requirement, name='delete_customer_requirement'),
    path('customer-final-requirements/', views.customer_final_requirements, name='customer_final_requirements'),
    path('logout/', views.custom_logout, name='logout'),

]
