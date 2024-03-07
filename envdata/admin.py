

from django.contrib import admin
from envdata.models import (Company, Fuel, Sf6, Refrigerant, Energy, Travel, Waste,Target)

# Register your models here.
admin.site.register(Company)
admin.site.register(Fuel)
admin.site.register(Sf6)
admin.site.register(Refrigerant)
admin.site.register(Energy)
admin.site.register(Travel)
admin.site.register(Waste)
admin.site.register(Target)
