from django.urls import path
from .views import *

urlpatterns = [
    #path("admin/", admin.site.urls),
    path('',patientDetails),
    path('patients/', PatientDetailsView.as_view(), name='patient_details'),
    path('patients/<int:patient_id>/', PatientDetailsView.as_view(), name='edit_patient_details'),
]
