from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.db.models import Max

from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime

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
        today = datetime.today()
        queues = self.filter(date__date=today).order_by('date')
        for index, queue in enumerate(queues, start=1):
            queue.quePos = index
            queue.save()

class PatientQueue(models.Model):
    patient = models.OneToOneField(PatientDetails,on_delete=models.CASCADE)
    quePos = models.IntegerField(blank=False,null=False)
    status = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)
    objects = PatientQueueManager()

    def __str__(self):
        return self.patient.patient_name + " @ " + str(self.quePos)

    def save(self, *args, **kwargs):
        if not self.pk:  # Only set quePos for new instances
            today = datetime.today()
            last_queue = PatientQueue.objects.filter(date__date=today).aggregate(Max('quePos'))
            max_que_pos = last_queue['quePos__max']
            self.quePos = (max_que_pos or 0) + 1
        super().save(*args, **kwargs)


### signals ###

@receiver(post_save, sender=PatientDetails)
def add_to_queue(sender, instance, created, **kwargs):
    if created:  # Check if a new instance is created
        PatientQueue.objects.create(patient=instance)
