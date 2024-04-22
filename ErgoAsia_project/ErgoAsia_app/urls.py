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
from ErgoAsia_app import views

urlpatterns = [
    path('ErgoAsiahome',views.ErgoAsiahome,name="ErgoAsiahome"),
    path('home',views.home,name="home"),
    path('',views.home,name="home1"),
    path('dashboard',views.dashboard,name="dashboard"),
    path('registrationtable',views.registrationtable,name="registrationtable"),
    path('ergoasiasignin',views.ergoasiasignin,name="ergoasiasignin"),
    path('notifications',views.notifications,name="notifications"),
    path('supplier',views.supplier,name="supplier"),
    path('edit/<int:pk>',views.DisplayModel,name="supplier"),








   


]
