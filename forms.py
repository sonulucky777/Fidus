from django import forms
from .models import UserProfileInfo, Prescription, MedicalTest
from django.contrib.auth.models import User
YEARS= [x for x in range(1960,2021)]

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    birth_date= forms.DateField(label='What is your birth date?', widget=forms.SelectDateWidget(years=YEARS))
    gender_choices = [("M", "Male"), ("F", "Female"), ("O", "Others")]
    gender = forms.TypedChoiceField(choices=gender_choices, initial="M")
    address = forms.CharField(max_length=300)
    zip_code = forms.CharField(max_length=12)
    phone = forms.CharField(max_length=20)
    class Meta():
        model = User
        fields = ('first_name','last_name','username','password','email','birth_date','address','zip_code','phone')

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('Social_link','profile_pic')

class PrescriptionForm(forms.ModelForm):
    class Meta: 
        model = Prescription 
        fields = "__all__"
class MedicalTestForm(forms.ModelForm):
    class Meta: 
        model = MedicalTest 
        fields = "__all__"
