import site

from django.contrib import admin
from envdata.models import Emission, FuelEmission

# Register your models here.
admin.site.register(Emission)
admin.site.register(FuelEmission)

