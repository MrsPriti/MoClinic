from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.
class PatientDetails(models.Model):

    patientid = models.BigAutoField(_("patient id"),primary_key=True)
    name = models.CharField(_("Name"), max_length=50,blank=False,null=False)
    mobile = models.CharField(_("Mobile Number"), max_length=13,blank=False,null=False)
    age = models.IntegerField(_("Age"),blank=False,null=False)
    height = models.FloatField(_("height"))
    symptom = models.TextField(_("Symptoms"),default="Regular Checkup")
