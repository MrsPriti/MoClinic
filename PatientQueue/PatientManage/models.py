from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.db.models import Max
# Create your models here.
class PatientDetails(models.Model):
    patient_name = models.CharField(max_length=255)
    patient_age = models.PositiveIntegerField()
    patient_mobile = models.CharField(max_length=15)
    weight = models.FloatField()
    height = models.FloatField()
    blood_pressure = models.FloatField()
    temperature = models.FloatField()
    blood_sugar = models.FloatField()
    heart_rate = models.FloatField()
    oxygen_level = models.FloatField()
    pulse_rate = models.FloatField()
    patient_symptoms = models.TextField()

    def __str__(self):
        return self.patient_name


class PatientQueueManager(models.Manager):
    def reset_queue_positions(self):
        today = timezone.now().date()
        queues = self.filter(date__date=today).order_by('date')
        for index, queue in enumerate(queues, start=1):
            queue.quePos = index
            queue.save()

class PatientQueue(models.Model):
    patient = models.OneToOneField(PatientDetails,on_delete=models.CASCADE)
    quePos = models.IntegerField(blank=False,null=False)
    date = models.DateTimeField(auto_now_add=True)
    objects = PatientQueueManager()

    def save(self, *args, **kwargs):
        if not self.pk:  # Only set quePos for new instances
            today = timezone.now().date()
            last_queue = PatientQueue.objects.filter(date__date=today).aggregate(Max('quePos'))
            max_que_pos = last_queue['quePos__max']
            self.quePos = (max_que_pos or 0) + 1
        super().save(*args, **kwargs)



