import uuid

from django.db import models
from envdata.models import Company
from envdata.constants import *
from users.models import Profile


# Create your models here.

class HealthAndSafety(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    month = models.CharField(blank=False, null=False, choices=MONTH)
    year = models.CharField(blank=False, null=False, max_length=4)

    total_working_hours = models.FloatField(blank=False, null=False, max_length=25)
    fatality_rate = models.FloatField(blank=False, null=False, max_length=10)
    high_consequence_rate = models.FloatField(blank=False, null=False, max_length=10)
    recordable_rate = models.FloatField(blank=False, null=False, max_length=10)

    ep_total_working_hours = models.FloatField(blank=False, null=False, max_length=25)
    ep_fatality_rate = models.FloatField(blank=False, null=False, max_length=10)
    ep_high_consequence_rate = models.FloatField(blank=False, null=False, max_length=10)
    ep_recordable_rate = models.FloatField(blank=False, null=False, max_length=10)

    total_training_hours = models.FloatField(blank=False, null=False, max_length=25)

    management_training_hours = models.FloatField(blank=False, null=False, max_length=25)
    operational_training_hours = models.FloatField(blank=False, null=False, max_length=25)

    women_management_training_hours = models.FloatField(blank=False, null=False, max_length=25)
    women_operational_training_hours = models.FloatField(blank=False, null=False, max_length=25)
    man_management_training_hours = models.FloatField(blank=False, null=False, max_length=25)
    man_operational_training_hours = models.FloatField(blank=False, null=False, max_length=25)

    id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False, primary_key=True)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.company}'
