from django.contrib import admin
from esgmanager.models import ESGPillars, ESGActionPlan, ESGActionPlanObjectives, ESGActionPlanActions, \
    NetZeroBusinessPlan, EnvironmentalRisk, GovernanceRisks, ClimateChangeRisk, SocialRisk

admin.site.register(ESGPillars)
admin.site.register(ESGActionPlan)
admin.site.register(ESGActionPlanObjectives)
admin.site.register(ESGActionPlanActions)
admin.site.register(NetZeroBusinessPlan)
admin.site.register(EnvironmentalRisk)
admin.site.register(GovernanceRisks)
admin.site.register(ClimateChangeRisk)
admin.site.register(SocialRisk)
