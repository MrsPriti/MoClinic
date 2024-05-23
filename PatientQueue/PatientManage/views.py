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

def patientDetails(request):
    return render(request,'patients.html')


def doctorDashboard(request):
    return render(request,'dr_d3.html')


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
                return redirect('patientDetails')
        else:
            return redirect('index')
    else:
        return redirect('index')

def signout(request):
    logout(request)
    return redirect('index')
# API views
@method_decorator(csrf_exempt, name='dispatch')
class PatientDetailsView(View):
    def get(self, request, *args, **kwargs):
        # Get all patient details
        patients = PatientDetails.objects.all()
        data = [{'patientid': patient.patientid,
                 'name': patient.name,
                 'mobile': patient.mobile,
                 'age': patient.age,
                 'symptom': patient.symptom} for patient in patients]
        return JsonResponse(data, safe=False)

    def post(self, request, *args, **kwargs):
        # Add new patient
        data = request.POST
        print(data)
        new_patient = PatientDetails.objects.create(
            name=data.get('name'),
            mobile=data.get('mobile'),
            age=data.get('age'),
            symptom=data.get('symptom', 'Regular Checkup')
        )
        return JsonResponse({'patientid': new_patient.patientid}, status=201)

    def put(self, request, *args, **kwargs):
        # Edit patient details
        data = request.POST
        patient_id = kwargs.get('patient_id')
        try:
            patient = PatientDetails.objects.get(patientid=patient_id)
            patient.name = data.get('name', patient.name)
            patient.mobile = data.get('mobile', patient.mobile)
            patient.age = data.get('age', patient.age)
            patient.symptom = data.get('symptom', patient.symptom)
            patient.save()
            return JsonResponse({'message': 'Patient details updated successfully'})
        except PatientDetails.DoesNotExist:
            return JsonResponse({'error': 'Patient not found'}, status=404)
