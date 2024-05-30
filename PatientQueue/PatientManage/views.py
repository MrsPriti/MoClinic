from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .models import PatientDetails
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
# Create your views here.


#render views
def index(request):
    return render(request,'index.html')

def add_patient(request):
    if request.method == 'POST':
        patient_name = request.POST.get('patient_name')
        patient_age = request.POST.get('patient_age')
        patient_mobile = request.POST.get('patient_mobile')
        weight = request.POST.get('weight')
        height = request.POST.get('height')
        blood_pressure = request.POST.get('blood_pressure')
        temperature = request.POST.get('temperature')
        blood_sugar = request.POST.get('blood_sugar')
        heart_rate = request.POST.get('heart_rate')
        oxygen_level = request.POST.get('oxygen_level')
        pulse_rate = request.POST.get('pulse_rate')
        patient_symptoms = request.POST.get('patient_symptoms')

        patient = PatientDetails.objects.create(
            patient_name=patient_name,
            patient_age=patient_age,
            patient_mobile=patient_mobile,
            weight=weight,
            height=height,
            blood_pressure=blood_pressure,
            temperature=temperature,
            blood_sugar=blood_sugar,
            heart_rate=heart_rate,
            oxygen_level=oxygen_level,
            pulse_rate=pulse_rate,
            patient_symptoms=patient_symptoms,
        )
        #patient.save()
        return redirect('staffDashboard')
    return render(request, 'staffs.html')


def get_patient(request):
    patients = PatientDetails.objects.all().values()
    patient_list = []
    for patient in patients:
        patient_list.append({
            'patient_name': patient['patient_name'],
            'patient_age': patient['patient_age'],
            'patient_mobile': patient['patient_mobile'],
            'weight': patient['weight'],
            'height': patient['height'],
            'blood_pressure': patient['blood_pressure'],
            'temperature': patient['temperature'],
            'blood_sugar': patient['blood_sugar'],
            'heart_rate': patient['heart_rate'],
            'oxygen_level': patient['oxygen_level'],
            'pulse_rate': patient['pulse_rate'],
            'patient_symptoms': patient['patient_symptoms'],
        })
    return JsonResponse({'patients': patient_list})



def doctorDashboard(request):
    return render(request,'dr_d3.html')

def staffDashboard(request):
    return render(request,'staffs.html')

def patientQueue(request):
    return render(request,"queueposition.html")


def signin(request):
    if request.method=='POST':
        username = request.POST.get('username','')
        pwd = request.POST.get('password','')
        user = authenticate(username=username,password=pwd)
        if user is not None:
            login(request,user)
            if user.is_staff:
                return redirect('doctorDashboard')
            else:
                return redirect('staffDashboard')
        else:
            return redirect('index')
    else:
        return redirect('index')

def signout(request):
    logout(request)
    return redirect('index')




# API views
