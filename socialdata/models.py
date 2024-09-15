import uuid

from django.db import models
from envdata.models import Company
from envdata.constants import *
from users.models import Profile


# Create your models here.


class SocialBaseClass(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    year = models.CharField(blank=False, null=False, max_length=4)
    id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False, primary_key=True)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    class Meta:
        abstract = True


class EmployeeAgeBaseClass(models.Model):
    county = models.CharField(blank=False, null=False, choices=COUNTY_CHOICES,max_length=255)
    men_under_30 = models.IntegerField(blank=False, null=False)
    women_under_30 = models.IntegerField(blank=False, null=False)
    men_between_30_and_50 = models.IntegerField(blank=False, null=False)
    women_between_30_and_50 = models.IntegerField(blank=False, null=False)
    men_over_50 = models.IntegerField(blank=False, null=False)
    women_over_50 = models.IntegerField(blank=False, null=False)

    @property
    def get_employee_under_30(self):
        return self.men_under_30 + self.women_under_30

    @property
    def get_employee_between_30_and_50(self):
        return self.men_between_30_and_50 + self.women_between_30_and_50

    @property
    def get_employee_over_50(self):
        return self.men_over_50 + self.women_over_50

    class Meta:
        abstract = True


class HealthAndSafety(SocialBaseClass):
    month = models.CharField(blank=False, null=False, choices=MONTH,max_length=25)
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


class EmployeeByContracts(SocialBaseClass):
    county = models.CharField(blank=False, null=False, choices=COUNTY_CHOICES,max_length=255)
    full_time_women = models.IntegerField(blank=False, null=False)
    full_time_men = models.IntegerField(blank=False, null=False)
    fixed_term_contract_women = models.IntegerField(blank=False, null=False)
    fixed_term_contract_men = models.IntegerField(blank=False, null=False)
    part_time_women = models.IntegerField(blank=False, null=False)
    part_time_men = models.IntegerField(blank=False, null=False)

    @property
    def get_total_full_time_contracts(self):
        return self.full_time_men + self.full_time_women

    @property
    def get_total_fixed_term_contracts(self):
        return self.fixed_term_contract_men + self.fixed_term_contract_women

    @property
    def get_total_part_time_contracts(self):
        return self.part_time_men + self.part_time_women


class NewEmployeeByAge(EmployeeAgeBaseClass, SocialBaseClass):
    pass


class RotationRateOfEmployeeByAge(EmployeeAgeBaseClass, SocialBaseClass):
    pass


class RetirementRate(SocialBaseClass):
    county = models.CharField(blank=False, null=False, max_length=255)
    retiring_next_10_years_management = models.IntegerField(blank=False, null=False)
    retiring_next_5_years_management = models.IntegerField(blank=False, null=False)
    retiring_next_10_years_operational = models.IntegerField(blank=False, null=False)
    retiring_next_5_years_operational = models.IntegerField(blank=False, null=False)

    @property
    def get_total_retired_10_years(self):
        return self.retiring_next_10_years_operational + self.retiring_next_10_years_management

    @property
    def get_total_retired_5_years(self):
        return self.retiring_next_5_years_operational + self.retiring_next_5_years_management
