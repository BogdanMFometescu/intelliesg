import uuid

from django.db import models
from envdata.models import Company


# Create your models here.

class HealthAndSafety(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False, primary_key=True)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
