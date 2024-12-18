from django.contrib import admin
from envdata.models import (Fuel, Sf6, Refrigerant, Energy, Travel, Waste, Target, NaturalGas,
                            TaxonomySector,TaxonomyTurnover,TaxonomyCapEx,TaxonomyOpEx,)


# Register your models here.

admin.site.register(Fuel)
admin.site.register(Sf6)
admin.site.register(Refrigerant)
admin.site.register(Energy)
admin.site.register(Travel)
admin.site.register(Waste)
admin.site.register(Target)
admin.site.register(NaturalGas)
admin.site.register(TaxonomySector)
admin.site.register(TaxonomyTurnover)
admin.site.register(TaxonomyCapEx)
admin.site.register(TaxonomyOpEx)
