from django.contrib import admin
from esgmanager.models import ESGPillars, ESGActionPlan, ESGActionPlanObjectives, ESGActionPlanActions, \
    NetZeroBusinessPlan

# Register your models here.

admin.site.register(ESGPillars)
admin.site.register(ESGActionPlan)
admin.site.register(ESGActionPlanObjectives)
admin.site.register(ESGActionPlanActions)
admin.site.register(NetZeroBusinessPlan)
