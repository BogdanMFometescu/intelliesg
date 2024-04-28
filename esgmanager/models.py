from django.db import models
from envdata.models import Company
import uuid


# Create your models here.

class ESGPillars(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    pillar = models.CharField(blank=False, null=False, max_length=255)
    description = models.TextField(blank=False, null=False)

    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, unique=True)

    def __str__(self):
        return f'{self.pillar}'


class ESGActionPlan(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    pillar = models.ForeignKey(ESGPillars, on_delete=models.CASCADE)
    plan_name = models.CharField(null=False, blank=False, max_length=255)
    start_date = models.DateField(blank=False, null=False)
    end_date = models.DateField(blank=False, null=False)

    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, unique=True)

    def __str__(self):
        return f'{self.plan_name}'


class ESGActionPlanObjectives(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    pillar = models.ForeignKey(ESGPillars, on_delete=models.CASCADE)
    plan = models.ForeignKey(ESGActionPlan, on_delete=models.CASCADE)
    objective = models.CharField(blank=False, null=False, max_length=255)
    description = models.TextField(blank=False, null=False)
    start_date = models.DateField(blank=False, null=False)
    end_date = models.DateField(blank=False, null=False)
    responsible = models.CharField(blank=False, null=False, max_length=255)
    status = models.CharField(blank=False, null=False, max_length=255)
    completion = models.FloatField(blank=False, null=False, default=0, )

    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, unique=True)

    def __str__(self):
        return f'{self.objective}'


class ESGActionPlanActions(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    pillar = models.ForeignKey(ESGPillars, on_delete=models.CASCADE)
    plan = models.ForeignKey(ESGActionPlan, on_delete=models.CASCADE)
    objective = models.ForeignKey(ESGActionPlanObjectives, on_delete=models.CASCADE)
    action = models.CharField(blank=False, null=False, max_length=255)
    description = models.TextField(blank=False, null=False)
    start_date = models.DateField(blank=False, null=False)
    end_date = models.DateField(blank=False, null=False)
    responsible = models.CharField(blank=False, null=False, max_length=255)
    status = models.CharField(blank=False, null=False, max_length=255)
    completion = models.FloatField(blank=False, null=False, default=0, )

    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, unique=True)

    def __str__(self):
        return f'{self.action}'


class NetZeroBusinessPlan(models.Model):
    pass
