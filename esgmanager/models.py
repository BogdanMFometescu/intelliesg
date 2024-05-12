from django.db import models
from envdata.models import Company
from datetime import date
import uuid
from esgmanager.constants import *


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

    @property
    def current_status(self):
        if self.end_date > date.today():
            return 'On track'
        return 'Delayed'

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

    @property
    def current_status(self):
        if self.end_date > date.today():
            return 'On track'
        return 'Delayed'

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

    @property
    def current_status(self):
        if self.end_date > date.today():
            return 'On track'
        return 'Delayed'

    def __str__(self):
        return f'{self.action}'


class NetZeroBusinessPlan(models.Model):
    pass


class EnvironmentalRisk(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    category = models.CharField(blank=False, null=False, max_length=255, choices=ENV_CATEGORY_CHOICES,
                                )
    risk = models.CharField(blank=False, null=False, max_length=255)
    description = models.TextField(blank=False, null=False, default='description')
    probability = models.PositiveSmallIntegerField(help_text="Scale from 1 (Low) to 10 (High)", blank=False, null=False,
                                                   default=1)
    severity = models.PositiveSmallIntegerField(help_text="Scale from 1 (Low) to 10 (High)", blank=False, null=False,
                                                default=1)
    mitigation_measures = models.TextField(blank=False, null=False, default='mitigation measure')
    opportunities = models.TextField(blank=True, null=True, default='opportunities')
    responsible = models.CharField(blank=False, null=False, max_length=255, default='responsible')
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, unique=True)
    updated = models.DateField(auto_now=True)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.risk}'

    @property
    def get_risk_impact(self):
        low = 1
        medium = 2
        impact = ((self.probability * 0.25) / 100 + (self.severity * 0.75) / 100) / 2
        if impact <= low:
            return 'Low'
        elif low < impact <= medium:
            return 'Medium'
        else:
            return 'High'

    class Meta:
        verbose_name = "Environmental Risk"
        verbose_name_plural = "Environmental Risks"


class ClimateChangeRisk(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    cc_category = models.CharField(blank=False, null=False, max_length=255, choices=CC_CATEGORY_CHOICES, )
    cc_risk = models.CharField(blank=False, null=False, max_length=255)
    cc_description = models.TextField(blank=False, null=False, default='description')
    cc_probability = models.PositiveSmallIntegerField(help_text="Scale from 1 (Low) to 10 (High)", blank=False,
                                                      null=False,
                                                      default=1)
    cc_severity = models.PositiveSmallIntegerField(help_text="Scale from 1 (Low) to 10 (High)", blank=False, null=False,
                                                   default=1)
    cc_mitigation_measures = models.TextField(blank=False, null=False, default='mitigation measure')
    cc_opportunities = models.TextField(blank=True, null=True, default='opportunities')
    cc_responsible = models.CharField(blank=False, null=False, max_length=255, default='responsible')
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, unique=True)
    updated = models.DateField(auto_now=True)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.cc_risk}'

    @property
    def get_risk_impact(self):
        low = 1
        medium = 2
        impact = ((self.cc_probability * 0.25) / 100 + (self.cc_severity * 0.75) / 100) / 2
        if impact <= low:
            return 'Low'
        elif low < impact <= medium:
            return 'Medium'
        else:
            return 'High'

    class Meta:
        verbose_name = "Climate Change Risk"
        verbose_name_plural = "Climate Change Risks"


class SocialRisk(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    soc_category = models.CharField(blank=False, null=False, max_length=255, choices=SOCIAL_CATEGORY_CHOICES,
                                    )
    soc_risk = models.CharField(blank=False, null=False, max_length=255)
    soc_description = models.TextField(blank=False, null=False, default='description')
    soc_probability = models.PositiveSmallIntegerField(help_text="Scale from 1 (Low) to 10 (High)", blank=False,
                                                       null=False,
                                                       default=1)
    soc_severity = models.PositiveSmallIntegerField(help_text="Scale from 1 (Low) to 10 (High)", blank=False,
                                                    null=False,
                                                    default=1)
    soc_mitigation_measures = models.TextField(blank=False, null=False, default='mitigation measure')
    soc_opportunities = models.TextField(blank=True, null=True, default='opportunities')
    soc_responsible = models.CharField(blank=False, null=False, max_length=255, default='responsible')
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, unique=True)
    updated = models.DateField(auto_now=True)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.soc_risk}'

    @property
    def get_risk_impact(self):
        low = 1
        medium = 2
        impact = ((self.soc_probability * 0.25) / 100 + (self.soc_severity * 0.75) / 100) / 2
        if impact <= low:
            return 'Low'
        elif low < impact <= medium:
            return 'Medium'
        else:
            return 'High'

    class Meta:
        verbose_name = "Social Risk"
        verbose_name_plural = "Social Risks"


class GovernanceRisks(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    gov_category = models.CharField(blank=False, null=False, max_length=255, choices=GOV_CATEGORY_CHOICES,
                                    default='category')
    gov_risk = models.CharField(blank=False, null=False, max_length=255)
    gov_description = models.TextField(blank=False, null=False, default='description')
    gov_probability = models.PositiveSmallIntegerField(help_text="Scale from 1 (Low) to 10 (High)", blank=False,
                                                       null=False,
                                                       default=1)
    gov_severity = models.PositiveSmallIntegerField(help_text="Scale from 1 (Low) to 10 (High)", blank=False,
                                                    null=False,
                                                    default=1)
    gov_mitigation_measures = models.TextField(blank=False, null=False, default='mitigation measure')
    gov_opportunities = models.TextField(blank=True, null=True, default='opportunities')
    gov_responsible = models.CharField(blank=False, null=False, max_length=255, default='responsible')
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, unique=True)
    updated = models.DateField(auto_now=True)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.gov_risk}'

    @property
    def get_risk_impact(self):
        low = 1
        medium = 2
        impact = ((self.gov_probability * 0.25) / 100 + (self.gov_severity * 0.75) / 100) / 2
        if impact <= low:
            return 'Low'
        elif low < impact <= medium:
            return 'Medium'
        else:
            return 'High'

    class Meta:
        verbose_name = "Governance Risk"
        verbose_name_plural = "Governance Risks"
