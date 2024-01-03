from django.db import models

class Update_profile_doctor(models.Model):
    user_id = models.CharField(max_length=30, default='')
    user_name=models.CharField(max_length=30,default='')
    name=models.CharField(max_length=30,default='')
    profile_picture = models.ImageField(default='default.jpg', upload_to='profile_pictures')
    department=models.CharField(max_length=30,default='')
    start_time=models.CharField(max_length=20,default='')
    end_time=models.CharField(max_length=20,default='')
    location=models.CharField(max_length=50,default='')
    hospital_name=models.CharField(max_length=50,default='')
    qualification=models.CharField(max_length=100,default='')
    institute =models.CharField(max_length=50,default='')
    email = models.CharField(max_length=50, default='')
    contact = models.CharField(max_length=50, default='')



class Diabetes_info(models.Model):
    user_name = models.CharField(max_length=30, default='')
    user_id = models.CharField(max_length=30, default='')
    pregnancies = models.CharField(max_length=30, default='')
    glucose=models.CharField(max_length=30,default='')
    bp=models.CharField(max_length=30,default='')
    skin_thickness=models.CharField(max_length=30,default='')
    insulin=models.CharField(max_length=30,default='')
    bmi = models.CharField(max_length=20,default='')
    diabetes_pedigree_function = models.CharField(max_length=30, default='')
    age = models.CharField(max_length=20,default='')



class Add_doctor(models.Model):
    user_name = models.CharField(max_length=30, default='')
    user_id = models.CharField(max_length=30, default='')
    name = models.CharField(max_length=30, default='')
    address=models.CharField(max_length=30,default='')
    contact=models.CharField(max_length=30,default='')
    email=models.CharField(max_length=30,default='')
    gender=models.CharField(max_length=30,default='')
    age = models.CharField(max_length=20,default='')


from datetime import date

import datetime

class Take_appointment(models.Model):
    user_id = models.CharField(max_length=30, default='')
    user_name=models.CharField(max_length=30,default='')
    full_name=models.CharField(max_length=30,default='')
    contact_number=models.CharField(max_length=30,default='')
    email=models.CharField(max_length=20,default='')
    doctor_id = models.CharField(max_length=30, default='')
    message=models.CharField(max_length=20,default='')
    date = models.DateField(("Date"), default=date.today)
    time = models.TimeField(default=datetime.time(16, 00))