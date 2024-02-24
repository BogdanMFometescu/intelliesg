import site

from django.contrib import admin
from envdata.models import (Emission,
                            FuelEmission,
                            Sf6Emission,
                            RefrigerantEmission,
                            EnergyAcquisition,
                            Travel,
                            WasteCalculation)

# Register your models here.
admin.site.register(Emission)
admin.site.register(FuelEmission)
admin.site.register(Sf6Emission)
admin.site.register(RefrigerantEmission)
admin.site.register(EnergyAcquisition)
admin.site.register(Travel)
admin.site.register(WasteCalculation)
