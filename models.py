from django.db import models
from django.contrib.auth.models import User

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=300, default='DEFAULT VALUE', blank=True, null=True)
    gender_choices = [("M", "Male"), ("F", "Female"), ("O", "Others")]
    gender = models.CharField(choices=gender_choices, default="M", max_length=1)
    zip_code = models.CharField('Zip/Post Code', max_length=12,default='DEFAULT VALUE', blank=True, null=True)
    phone = models.CharField('Contact Phone', max_length=13, blank=True)
    Social_link = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return self.user.username
class Doctor(models.Model):
    doctor_name = models.CharField(max_length=30)
    registration_date = models.DateTimeField('date registered')
class Hospital(models.Model):
    hospital_name = models.CharField(max_length=30)
    h_address = models.CharField(max_length=100)

class Patient(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    hospital = models.ForeignKey(Hospital, default="", on_delete=models.CASCADE)
    patient_name = models.CharField(max_length=30)
    registration_date = models.DateTimeField("date registered")
    waiting_status = models.BooleanField()

    @property
    def is_waiting(self):
        return bool(self.waiting_status)

class Prescription(models.Model):
    patient = models.ForeignKey(User, related_name="patient", on_delete=models.CASCADE)
    doctor = models.ForeignKey(User, related_name="doctor", on_delete=models.CASCADE)
    date = models.DateField()
    medication = models.CharField(max_length=100)
    strength = models.CharField(max_length=30)
    instruction = models.CharField(max_length=200)
    refill = models.IntegerField()
    active = models.BooleanField(default=True)
class MedicalTest(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateField()
    description = models.CharField(max_length=200)
    doctor = models.ForeignKey(User, related_name="docs", on_delete=models.CASCADE)
    patient = models.ForeignKey(User, related_name="pts", on_delete=models.CASCADE)
    private = models.BooleanField(default=True)
    completed = models.BooleanField()