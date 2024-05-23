from django.urls import path
from .views import *

urlpatterns = [
    #path("admin/", admin.site.urls),
    path('',index,name='index'),
    path('patients/', PatientDetailsView.as_view(), name='patient_details'),
    path('patients/<int:patient_id>/', PatientDetailsView.as_view(), name='edit_patient_details'),
    path('doctorDashboard', doctorDashboard, name='doctorDashboard'),
    path('signin', signin, name='signin'),
    path('signout', signout, name='signout'),
    path("patientDetails",patientDetails,name="patientDetails")
]
