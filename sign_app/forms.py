from django import forms
from .models import UserProfileInfo, Prescription, MedicalTest, Appointment
from django.contrib.auth.models import User
YEARS= [x for x in range(1960,2022)]

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    #password_confirmation = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password')

class UserProfileInfoForm(forms.ModelForm):
    birth_date= forms.DateField(label='What is your birth date?', widget=forms.SelectDateWidget(years=YEARS))
    class Meta():
        model = UserProfileInfo
        fields = ('gender','birth_date','address','zip_code','phone','Social_link')

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = "__all__"
class PrescriptionForm(forms.ModelForm):
    class Meta: 
        model = Prescription 
        fields = "__all__"
class MedicalTestForm(forms.ModelForm):
    class Meta: 
        model = MedicalTest 
        fields = "__all__"
