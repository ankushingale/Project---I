from django.contrib import admin
from django.urls import path
from customer_app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('customerhome', views.customerhome, name="customerhome"),
    path('customer-signup', views.customersignup, name="customersignup"),
    path('customer-requirements', views.customerrequirements, name='customer-requirements'),
    path('customer-tables', views.customertables, name='customer-tables'), 
    path('customer-sign', views.customersignin, name="customersign"),
    path('customer-dashboard', views.customerdashboard, name="Cdashboard"),
    path('customer-profile', views.customerprofile, name="customerprofile"),
    path('edit/<int:pk>', views.displayModel, name="customereditmodel"),
    path('model_category/<int:customer_id>/<str:category>/', views.categorymodel, name='model_category'),
    path('edit_requirement/<int:project_id>/', views.edit_customer_requirement, name='edit_customer_requirement'),
    path('delete_requirement/<int:project_id>/', views.delete_customer_requirement, name='delete_customer_requirement'),
    path('customer-final-requirements/', views.customer_final_requirements, name='customer_final_requirements'),
    path('logout/', views.custom_logout, name='logout'),

    # New paths for filtering final requirements
    path('final-requirements/', views.final_requirement_list, name='final_requirement_list'),
    path('final-requirements/status/<str:status>/', views.final_requirement_list, name='final_requirement_list_filtered'),
]
