"""doctor1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

from user import views as views1
#from product import views as viewsprod
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',views1.register,name='register'),
    path('base/',views1.base),
    path('home/',views1.home,name='home'),
    path('',auth_views.LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='user/logout.html'), name='logout'),
    path('user/',views1.user,name='user'),

    path('update_profile_doctor/',views1.update_profile_doctor,name='update_profile_doctor'),
    path('create_profile_doctor/',views1.create_profile_doctor,name='create_profile_doctor'),
    path('take_appointment/',views1.take_appointment,name='take_appointment'),

    path('my_appointment/',views1.my_appointment,name='my_appointment'),
    path('test/', views1.test, name='test'),
    path('doctor/', views1.doctor, name='doctor'),
    path('docprofile/', views1.docprofile, name='docprofile'),
    path('appointments/', views1.appointments, name='appointments'),
    path('diabetes_info/', views1.diabetes_info, name='diabetes_info'),

    path('add_doctor/', views1.add_doctor, name='add_doctor'),
    path('all_doctors/', views1.all_doctors, name='all_doctors'),
    path('all_appointments/', views1.all_appointments, name='all_appointments'),

    path('doctor_home/', views1.doctor_home, name='doctor_home'),
    path('admin_home/', views1.admin_home, name='admin_home'),
    path('patient_home/', views1.patient_home, name='patient_home'),

    path('shell/', views1.shell, name='shell'),


]
