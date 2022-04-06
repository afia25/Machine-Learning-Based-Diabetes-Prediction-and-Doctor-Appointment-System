from django.db import models

class Update_profile_doctor(models.Model):
    user_id = models.CharField(max_length=30, default='')
    user_name=models.CharField(max_length=30,default='')
    name=models.CharField(max_length=30,default='')
    department=models.CharField(max_length=30,default='')
    start_time=models.CharField(max_length=20,default='')
    end_time=models.CharField(max_length=20,default='')
    location=models.CharField(max_length=50,default='')
    hospital_name=models.CharField(max_length=50,default='')
    qualification=models.CharField(max_length=100,default='')
    institute =models.CharField(max_length=50,default='')
    email = models.CharField(max_length=50, default='')
    contact = models.CharField(max_length=50, default='')


class Take_appointment(models.Model):
    user_id = models.CharField(max_length=30, default='')
    user_name=models.CharField(max_length=30,default='')
    full_name=models.CharField(max_length=30,default='')
    contact_number=models.CharField(max_length=30,default='')
    email=models.CharField(max_length=20,default='')
    doctor_id = models.CharField(max_length=30, default='')
    message=models.CharField(max_length=20,default='')
