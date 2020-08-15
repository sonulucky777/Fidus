from django.shortcuts import render, redirect
from .forms import UserForm, UserProfileInfoForm #AppointmentForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import *

def index(request):
    return render(request, 'sign_app/index.html')

@login_required
def special(request):
    return HttpResponse('You are logged in !')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                    print('found it')
                    profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request,'sign_app/registration.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered})
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse('Your account was inactive.')
        else:
            print("Someone tried to login and failed")
            print("they used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'sign_app/login.html', {})

# def home(request):
#     appointments = Appointment.objects.all()
#     hospitals = Hospital.objects.all()
#     total_hospitals = hospitals.count()
#     total_appointments = appointments.count()
#     conformed = appointments.filter(status='Conformed').count()
#     pending = appointments.filter(status='Pending').count()
    
#     context = {'appointments':appointments, 'hospitals':hospitals,
# 	'total_appointments':total_appointments,'conformed':conformed,
# 	'pending':pending }
#     return render(request, 'sign_app/base_appoint.html', context)

# def doctors(request):
#     doctors = Doctor.objects.all()

#     return render(request, 'sign_app/doctors.html', {'doctors':doctors})

# def hospitals(request, pk):
#     hospitals = Hospital.objects.get(id=pk)
#     appointments = hospitals.appointment_set.all()
#     appointment_count = appointments.count()

#     context = {'hospitals':hospitals, 'appointments':appointments, 'appointment_count':appointment_count}
#     return render(request, 'sign_app/hospitals.html',context)

# def createAppointment(request):
#     form = AppointmentForm()
#     if request.method == 'POST':
#         form = AppointmentForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/')
#     context = {'form':form}
#     return render(request, 'sign_app/appointment_form.html', context)

# def updateAppointment(request, pk):
#     appointment = Appointment.objects.get(id=pk)
#     form = AppointmentForm(instance=appointment)

#     if request.method == 'POST':
#         form = AppointmentForm(request.POST, instance=appointment)
#         if form.is_valid():
#             form.save()
#             return redirect('/')

#     context = {'form':form}
#     return render(request, 'sign_app/appointment_form.html', context)

# def deleteAppointment(request, pk):
#     appointment = Appointment.objects.get(id=pk)
#     if request.method == 'POST':
#         appointment.delete()
#         return redirect('/')
#     context = {'item':appointment}
#     return render(request, 'sign_app/delete.html', context)


# if User.objects.filter(username=user_form.cleaned_data['username']).exists():
#                 return render(request,'sign_app/registration.html',
#                           {'user_form':user_form,
#                            'error_message':'Username already exists.'})
#             elif User.objects.filter(email=user_form.cleaned_data['email']).exists():
#                 return render(request,'sign_app/registration.html',
#                           {'user_form':user_form,
#                            'error_message':'Email already exists.'})
#             elif user_form.cleaned_data['password'] != user_form.cleaned_data['password_confirmation']:
#                 return render(request,'sign_app/registration.html',
#                           {'user_form':user_form,
#                            'error_message':'Passwords do not match.'})
#             else:
