from django.urls import path
from .views import *

urlpatterns = [
    #path("admin/", admin.site.urls),
    path('',index,name='index'),
    path('doctorDashboard', doctorDashboard, name='doctorDashboard'),
    path('signin', signin, name='signin'),
    path('signout', signout, name='signout'),
    path("staffDashboard",staffDashboard,name="staffDashboard"),
    path("add_patient",add_patient,name="add_patient"),
    path("get_patient",get_patient,name="get_patient"),
]
