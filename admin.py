from django.contrib import admin
from .models import UserProfileInfo, User, Doctor, Hospital, Appointment, Prescription, MedicalTest, Medical_history
from address.models import AddressField

# Register your models here.

class AppointmentInline(admin.TabularInline):
    model = Appointment
    extra = 0
class HospitalInline(admin.TabularInline):
    model = Hospital

class DoctorAdmin(admin.ModelAdmin):
    list_display = ['doctor_name']
    inlines = [AppointmentInline, HospitalInline]

admin.site.register(Doctor, DoctorAdmin)
admin.site.register(UserProfileInfo)
#admin.site.register(Doctor)
admin.site.register(Hospital)
admin.site.register(Appointment)
admin.site.register(Prescription)
admin.site.register(MedicalTest)
admin.site.register(Medical_history)