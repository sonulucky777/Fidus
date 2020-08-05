from django.contrib import admin
from .models import UserProfileInfo, User, Doctor, Hospital, Patient, Prescription, MedicalTest

# Register your models here.
admin.site.register(UserProfileInfo)

#class PatientInline(admin.TabularInline):
#    model = Patient
#    extra = 0

#class DoctorAdmin(admin.ModelAdmin):
 #   Inlines = [PatientInline]

admin.site.register(Doctor)
admin.site.register(Hospital)
admin.site.register(Patient)
admin.site.register(Prescription)
admin.site.register(MedicalTest)