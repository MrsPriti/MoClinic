from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime
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
    patients = PatientQueue.objects.filter(date__date=datetime.today().date())
    patient_list = []
    for pat in patients:
        patient_list.append({
            'patient_name': pat.patient.patient_name,
            'patient_age': pat.patient.patient_age,
            'patient_mobile': pat.patient.patient_mobile,
            'weight': pat.patient.weight,
            'height': pat.patient.height,
            'blood_pressure': pat.patient.blood_pressure,
            'temperature': pat.patient.temperature,
            'blood_sugar': pat.patient.blood_sugar,
            'heart_rate': pat.patient.heart_rate,
            'oxygen_level': pat.patient.oxygen_level,
            'pulse_rate': pat.patient.pulse_rate,
            'patient_symptoms': pat.patient.patient_symptoms,
            'pos':pat.quePos,
            'status':pat.status
        })
    return JsonResponse({'patients': patient_list})

def send_patient(request):
    patientId = request.GET.get('patientId',None)
    if patientId is not None:
        patient = PatientDetails.objects.get(id=patientId)
        queue = PatientQueue.objects.get(patient=patient)
        queue.status = 1
        queue.save()
        return redirect("staffDashboard")

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
