import uuid

from django.db import models
from envdata.models import Company


# Create your models here.

class HealthAndSafety(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    own_total_working_hours = models.FloatField(blank=False, null=False, max_length=25,default=0)
    own_fatality_rate = models.FloatField(blank=False, null=False, max_length=10,default=0)
    own_high_consequence_rate = models.FloatField(blank=False, null=False, max_length=10,default=0)
    own_recordable_rate = models.FloatField(blank=False, null=False, max_length=10,default=0)

    external_provider_total_working_hours = models.FloatField(blank=False, null=False, max_length=25,default=0)
    external_provider_fatality_rate = models.FloatField(blank=False, null=False, max_length=10,default=0)
    external_provider_high_consequence_rate = models.FloatField(blank=False, null=False, max_length=10,default=0)
    external_provider_recordable_rate = models.FloatField(blank=False, null=False, max_length=10,default=0)

    total_training_hours = models.FloatField(blank=False, null=False, max_length=25,default=0)
    management_training_hours = models.FloatField(blank=False, null=False, max_length=25,default=0)
    operational_training_hours = models.FloatField(blank=False, null=False, max_length=25,default=0)
    women_management_training_hours = models.FloatField(blank=False, null=False, max_length=25,default=0)
    women_operational_training_hours = models.FloatField(blank=False, null=False, max_length=25,default=0)
    man_management_training_hours = models.FloatField(blank=False, null=False, max_length=25,default=0)
    man_operational_training_hours = models.FloatField(blank=False, null=False, max_length=25,default=0)

    id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False, primary_key=True)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
