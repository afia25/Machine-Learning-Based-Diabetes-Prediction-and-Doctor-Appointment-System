from django.contrib.auth.models import User
from .models import *
from django.contrib.auth.forms import UserCreationForm , forms

class UserRegistrationForm(UserCreationForm):
    first_name=forms.CharField(max_length=40)
    last_name = forms.CharField(max_length=40)
    email = forms.EmailField()

class Meta:
    model=User
    fields=[
        'username',
        'first_name',
        'last_name',
        'email',
        'password1',
        'password2',
    ]

class CreateForm(forms.ModelForm):
    profile_picture = forms.ImageField(required=False)

    class Meta:
        model=Update_profile_doctor
        fields=[
            'user_id',
            'user_name',
            'name',
            'profile_picture',
            'department',
            'start_time',
            'end_time',
            'location',
            'hospital_name',
            'qualification',
            'institute',
            'email',
            'contact',

        ]


class TakeAppointmentForm(forms.ModelForm):
    message = forms.CharField(max_length=20, required=False)
    class Meta:
        model=Take_appointment
        fields=[
            'user_id',
            'user_name',
            'full_name',
            'contact_number',
            'email',
            'doctor_id',
            'message',
            'date',
            'time',



        ]



class AddDoctorForm(forms.ModelForm):
    class Meta:
        model=Add_doctor
        fields=[
            'user_name',
            'user_id',
            'name',
            'address',
            'contact',
            'email',
            'gender',
            'age',

        ]