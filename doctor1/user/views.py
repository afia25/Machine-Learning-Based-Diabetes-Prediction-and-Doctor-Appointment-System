from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .form import *
#from . import loaddata
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user,authenticate,login
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score





def test(request):
    if (request.method == 'POST'):
        data=pd.read_csv(r'D:\Desktop\soft dev lab\Diabetes Dataset\diabetes.csv')

        #train test split
        X=data.drop("Outcome" , axis=1)
        Y=data['Outcome']
        X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size=0.2)

        #training and predicting
        model=LogisticRegression()
        model.fit(X_train , Y_train)



        dict = request.POST
        v1 = dict['n1']
        v2 = dict['glucose']
        v3 = dict['bp']
        v4 = dict['st']
        v5 = dict['insulin']
        v6 = dict['bmi']
        v7 = dict['dpf']
        v8 = dict['age']

        val1 = float(v1)
        val2 = float(v2)
        val3 = float(v3)
        val4 = float(v4)
        val5 = float(v5)
        val6 = float(v6)
        val7 = float(v7)
        val8 = float(v8)

        user = get_user(request)
        un = user.username
        info = Diabetes_info(user_name=un,pregnancies=v1,glucose=v2,bp=v3,skin_thickness=v4,insulin=v5,bmi=v6,diabetes_pedigree_function=v7,age=v8)
        info.save()
        #prediction = model.predict([ [val1 ], [val2], [val3], [val4], [val5], [val6], [val7], [val8] ])
        #prediction = model.predict([ [val1,val2,val3,val4,val5,val6,val7,val8], [val1,val2,val3,val4,val5,val6,val7,val8], [val1,val2,val3,val4,val5,val6,val7,val8], [val1,val2,val3,val4,val5,val6,val7,val8], [val1,val2,val3,val4,val5,val6,val7,val8], [val1,val2,val3,val4,val5,val6,val7,val8], [val1,val2,val3,val4,val5,val6,val7,val8], [val1,val2,val3,val4,val5,val6,val7,val8] ])
        #prediction = model.predict([ [ val1 , val2, val3, val4, val5, val6, val7, val8 ] ])
        #prediction = model.predict(np.array([val1, val2, val3, val4, val5, val6, val7, val8]))

        prediction = model.predict(np.array([val1, val2, val3, val4, val5, val6, val7, val8]).reshape(1,-1))
        #prediction = model.predict(np.array([v1, v2, v3, v4, v5, v6, v7, v8]).reshape(1, -1))

        result = ""
        if prediction == [1]:
            result = "Positive"
        if prediction == [0]:
            result = "Negative"

        return render(request, 'user/test.html' , {"res" : result})

    return render(request, 'user/test.html')


def doctor(request):
    a = '301'
    b = '302'
    c = '303'
    doctora = Update_profile_doctor.objects.get(user_id__exact=a)
    doctorb = Update_profile_doctor.objects.get(user_id__exact=b)
    doctorc = Update_profile_doctor.objects.get(user_id__exact=c)
    context = {
        'doctora': doctora,
        'doctorb': doctorb,
        'doctorc': doctorc,
    }

    return render(request,'user/doctor.html', context)

def take_appointment(request):
    if (request.method=="POST"):
        take_appointment_form = TakeAppointmentForm(request.POST)
        if (take_appointment_form.is_valid()):
            take_appointment_form.save()
            return render(request, 'user/made_appointment.html')
        else:
            context = {
                'take_appointment_form': take_appointment_form,
            }
            return render(request, 'user/take_appointment.html', context)
    else:
        take_appointment_form = TakeAppointmentForm()
        context = {
            'take_appointment_form': take_appointment_form,
        }
        return render(request, 'user/take_appointment.html', context)



def my_appointment(request):
    if (request.method == 'POST'):
        dict = request.POST
        id = dict['id']
        c = Take_appointment.objects.get(id__exact=id)
        c.delete()

        a = '201'
        # get the obj which has max id. api django

        take_appointment = Take_appointment.objects.all()
        context = {
            'take_appointment': take_appointment,
            'a': a,
        }
        return render(request, 'user/my_appointment.html', context)

    else:
        a = '201'
        # get the obj which has max id. api django

        take_appointment = Take_appointment.objects.all()
        context = {
            'take_appointment': take_appointment,
            'a': a,
        }
        return render(request, 'user/my_appointment.html', context)



def create_profile_doctor(request):
    if (request.method=="POST"):
        createform = CreateForm(request.POST)
        if (createform.is_valid()):
            createform.save()
            return redirect('home')
        else:
            context = {
                'createform': createform,
            }
            return render(request, 'user/create_profile_doctor.html', context)
    else:
        createform = CreateForm()
        context = {
            'createform': createform,
        }
        return render(request, 'user/create_profile_doctor.html', context)


def update_profile_doctor(request):
    if (request.method=='POST'):
        dict=request.POST
        uid = dict['uid']
        profile = Update_profile_doctor.objects.get(user_id__exact=uid)
        #b=Products.objects.get(id__exact=a)

        unm = dict['unm']
        profile.user_name = unm
        nm = dict['nm']
        profile.name = nm
        dep = dict['dep']
        profile.department = dep
        st = dict['st']
        profile.start_time = st
        et = dict['et']
        profile.end_time = et
        loc = dict['loc']
        profile.location = loc
        hos = dict['hos']
        profile.hospital_name = hos
        q = dict['q']
        profile.qualification = q
        inst = dict['inst']
        profile.institute = inst
        e = dict['email']
        profile.email = e
        contact = dict['contact']
        profile.contact = contact


        profile.save()

        return render(request, 'user/update_profile_doctor.html', {'profile': profile})

    else:
        return render(request, 'user/update_profile_doctor.html')






def register(request):
    if (request.method=="POST"):
        form=UserRegistrationForm(request.POST)
        #profileform = RegistrationProfileForm(request.POST)
        #if (form.is_valid() and profileform.is_valid()):
        if (form.is_valid()):
            #error=''
            #dict=request.POST
            #username=dict['username']
            #check=User.objects.filter(username='username')
            #if len(check)==0:
            form.save()
            #profileform.save()

            #else:
                #error='Username already exists.'
                #return render(request, 'customer/register.html', {'form':form,'error':error})

            user = get_user(request)

            uname=form.cleaned_data.get('username')
            fname = form.cleaned_data.get('first_name')
            lname = form.cleaned_data.get('last_name')
            email = form.cleaned_data.get('email')
            psw = form.cleaned_data.get('password1')
            c = User.objects.get(username__exact=uname)
            c.first_name = fname
            c.last_name = lname
            c.email = email
            c.save()

            new_user=authenticate(username=uname,password=psw)
            login(request,new_user)

            # shows msg in home after registration
            #message='Welcome to Inventory Management System'
            #messages.success(request, message=message)
            return redirect('home')


        else:
            context={
                'form':form
            }
            return render(request, 'user/register.html', context)

    else:
        form = UserRegistrationForm()
        #profileform=RegistrationProfileForm()
        #return render(request, 'customer/register.html', {'form':form,'profileform':profileform})
        return render(request, 'user/register.html', {'form': form})


@login_required
def home(request):
    user = get_user(request)
    p=Update_profile_doctor.objects.all()
    context = {
        'name': user.username,
        'email': user.email,


    }
    #shows msg in home after login
    #message = 'Welcome to Inventory Management System'
    #messages.success(request, message=message)
    return render(request,'user/home.html', context)


def base(request):
    return render(request,'user/base.html')

def user(request):
    return render(request,'user/home.html')

def docprofile(request):
    user = get_user(request)
    un=user.username
    doctor = Update_profile_doctor.objects.get(user_name__exact=un)
    a='301'
    b='302'
    c='303'
    context = {
        'doctor': doctor,
        'a':a,
        'b':b,
        'c':c,
    }

    return render(request, 'user/docprofile.html', context)


def appointments(request):
    if (request.method == 'POST'):
        dict = request.POST
        a = dict['docid']
        take_appointment = Take_appointment.objects.all()
        context = {
            'take_appointment': take_appointment,
            'a': a,

        }
        return render(request, 'user/appointments.html', context)

    return render(request,'user/appointments.html')



def diabetes_info(request):
    if (request.method == 'POST'):
        dict = request.POST
        un = dict['un']
        diabetes_info = Diabetes_info.objects.get(user_name__exact=un)
        context = {
            'diabetes_info': diabetes_info,

        }
        return render(request, 'user/diabetes_info.html', context)

    return render(request,'user/diabetes_info.html')



def add_doctor(request):
    if (request.method=="POST"):
        add_doctor_form = AddDoctorForm(request.POST)
        if (add_doctor_form.is_valid()):
            add_doctor_form.save()
            return redirect('home')
        else:
            context = {
                'add_doctor_form': add_doctor_form,
            }
            return render(request, 'user/add_doctor.html', context)
    else:
        add_doctor_form = AddDoctorForm()
        context = {
            'add_doctor_form': add_doctor_form,
        }
        return render(request, 'user/add_doctor.html', context)


def all_doctors(request):
    if (request.method == 'POST'):
        dict = request.POST
        a = dict['docid']
        doctor = Add_doctor.objects.get(user_id__exact=a)
        doctor.delete()
        add_doctor = Add_doctor.objects.all()
        context = {
            'add_doctor': add_doctor,

        }
        return render(request, 'user/all_doctor.html', context)

    else:
        add_doctor = Add_doctor.objects.all()
        context = {
            'add_doctor': add_doctor,

        }
        return render(request, 'user/all_doctor.html', context)




def all_appointments(request):
    take_appointment = Take_appointment.objects.all()

    context = {
        'take_appointment': take_appointment,

    }
    return render(request, 'user/all_appointments.html', context)



def doctor_home(request):
    return render(request, 'user/doctor_home.html')

def admin_home(request):
    return render(request, 'user/admin_home.html')

def patient_home(request):
    return render(request, 'user/patient_home.html')


def shell(request):
    c = Take_appointment.objects.get(user_id__exact='103')
    #c.doctor_id='302'
    #c.save()
    c.delete()
    return render(request,'user/home.html')





