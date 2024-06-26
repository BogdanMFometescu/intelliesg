from django.contrib import admin
from socialdata.models import HealthAndSafety, NewEmployeeByAge, EmployeeByContracts, RotationRateOfEmployeeByAge, \
    RetirementRate

# Register your models here.

admin.site.register(HealthAndSafety)
admin.site.register(NewEmployeeByAge)
admin.site.register(EmployeeByContracts)
admin.site.register(RotationRateOfEmployeeByAge)
admin.site.register(RetirementRate)
