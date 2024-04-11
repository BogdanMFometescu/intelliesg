from django.db import transaction

from envdata.models import Company, Fuel, NaturalGas, Energy, Sf6, Refrigerant, Travel, Waste
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from openpyxl import load_workbook
from envdata.forms import ExcelUploadForm


class ExcelUploadView(FormView):
    form_class = ExcelUploadForm
    template_name = 'envdata/upload_excel/upload_fuel_data.html'
    success_url = reverse_lazy('fuel_emissions')

    def form_valid(self, form):
        excel_file = form.cleaned_data['excel_file']
        wb = load_workbook(filename=excel_file)
        sheet_name = 'fuel'
        if sheet_name in wb.sheetnames:
            ws = wb[sheet_name]
        else:
            return self.form_invalid(form)

        with transaction.atomic():
            for row in ws.iter_rows(min_row=2, values_only=True):
                company_name = row[0]
                if company_name:
                    company, created = Company.objects.get_or_create(name=company_name)
                    Fuel.objects.create(
                        company=company,
                        month=row[1],
                        year=row[2],
                        emission_type=row[3],
                        emission_scope=row[4],
                        fuel_type=row[5],
                        fuel_source=row[6],
                        fuel_quantity=row[7],
                        pollution_norm=row[8],
                        activity_type=row[9],
                        vehicle_type=row[10],
                        measure_unit=row[11],
                        emission_factor=row[12]
                    )
                else:

                    pass

        return super().form_valid(form)


class ExcelUploadViewForNaturalGas(FormView):
    form_class = ExcelUploadForm
    template_name = 'envdata/upload_excel/upload_natural_gas_data.html'
    success_url = reverse_lazy('gas_emissions')

    def form_valid(self, form):
        excel_file = form.cleaned_data['excel_file']
        wb = load_workbook(filename=excel_file)
        sheet_name = 'natural_gas'
        if sheet_name in wb.sheetnames:
            ws = wb[sheet_name]
        else:
            return self.form_invalid(form)

        with transaction.atomic():
            for row in ws.iter_rows(min_row=2, values_only=True):
                company_name = row[0]
                if company_name:
                    company, created = Company.objects.get_or_create(name=company_name)
                    NaturalGas.objects.create(
                        company=company,
                        month=row[1],
                        year=row[2],
                        emission_type=row[3],
                        emission_scope=row[4],
                        location=row[5],
                        gas_quantity=row[6],
                        emission_factor=row[7],
                        measure_unit=row[8]
                    )
                else:

                    pass

        return super().form_valid(form)


class ExcelUploadViewForEnergy(FormView):
    form_class = ExcelUploadForm
    template_name = 'envdata/upload_excel/upload_energy_data.html'
    success_url = reverse_lazy('energy_acquisitions')

    def form_valid(self, form):
        excel_file = form.cleaned_data['excel_file']
        wb = load_workbook(filename=excel_file)
        sheet_name = 'energy'
        if sheet_name in wb.sheetnames:
            ws = wb[sheet_name]
        else:
            return self.form_invalid(form)

        with transaction.atomic():
            for row in ws.iter_rows(min_row=2, values_only=True):
                company_name = row[0]
                if company_name:
                    company, created = Company.objects.get_or_create(name=company_name)
                    Energy.objects.create(
                        company=company,
                        month=row[1],
                        year=row[2],
                        emission_type=row[3],
                        emission_scope=row[4],
                        location=row[5],
                        supplier_name=row[6],
                        measure_unit=row[7],
                        energy_quantity=row[8],
                        emission_factor=row[9],
                        calculation_method=row[10]

                    )
                else:

                    pass

        return super().form_valid(form)


class ExcelUploadViewForSf6(FormView):
    form_class = ExcelUploadForm
    template_name = 'envdata/upload_excel/upload_sf6_data.html'
    success_url = reverse_lazy('sf6_emissions')

    def form_valid(self, form):
        excel_file = form.cleaned_data['excel_file']
        wb = load_workbook(filename=excel_file)
        sheet_name = 'sf6'
        if sheet_name in wb.sheetnames:
            ws = wb[sheet_name]
        else:
            return self.form_invalid(form)

        with transaction.atomic():
            for row in ws.iter_rows(min_row=2, values_only=True):
                company_name = row[0]
                if company_name:
                    company, created = Company.objects.get_or_create(name=company_name)
                    Sf6.objects.create(
                        company=company,
                        month=row[1],
                        year=row[2],
                        emission_type=row[3],
                        emission_scope=row[4],
                        equipment_type=row[5],
                        equipment_producer=row[6],
                        sf6_quantity=row[7],
                        emission_factor=row[8],
                    )
                else:

                    pass

        return super().form_valid(form)


class ExcelUploadViewForRefrigerant(FormView):
    form_class = ExcelUploadForm
    template_name = 'envdata/upload_excel/upload_sf6_data.html'
    success_url = reverse_lazy('refrigerant_emissions')

    def form_valid(self, form):
        excel_file = form.cleaned_data['excel_file']
        wb = load_workbook(filename=excel_file)
        sheet_name = 'refrigerant'
        if sheet_name in wb.sheetnames:
            ws = wb[sheet_name]
        else:
            return self.form_invalid(form)

        with transaction.atomic():
            for row in ws.iter_rows(min_row=2, values_only=True):
                company_name = row[0]
                if company_name:
                    company, created = Company.objects.get_or_create(name=company_name)
                    Refrigerant.objects.create(
                        company=company,
                        month=row[1],
                        year=row[2],
                        emission_type=row[3],
                        emission_scope=row[4],
                        refrigerant_type=row[5],
                        refrigerant_quantity=row[6],
                        emission_factor=row[7],
                    )
                else:

                    pass

        return super().form_valid(form)


class ExcelUploadViewForTravel(FormView):
    form_class = ExcelUploadForm
    template_name = 'envdata/upload_excel/upload_travel_data.html'
    success_url = reverse_lazy('travels')

    def form_valid(self, form):
        excel_file = form.cleaned_data['excel_file']
        wb = load_workbook(filename=excel_file)
        sheet_name = 'travels'
        if sheet_name in wb.sheetnames:
            ws = wb[sheet_name]
        else:
            return self.form_invalid(form)

        with transaction.atomic():
            for row in ws.iter_rows(min_row=2, values_only=True):
                company_name = row[0]
                if company_name:
                    company, created = Company.objects.get_or_create(name=company_name)
                    Travel.objects.create(
                        company=company,
                        month=row[1],
                        year=row[2],
                        emission_type=row[3],
                        emission_scope=row[4],
                        origin=row[5],
                        destination=row[6],
                        emission_factor=row[7],
                        distance=row[8],
                        fuel_consumption=row[9],
                    )
                else:

                    pass

        return super().form_valid(form)


class ExcelUploadViewForWaste(FormView):
    form_class = ExcelUploadForm
    template_name = 'envdata/upload_excel/upload_waste_data.html'
    success_url = reverse_lazy('wastes')

    def form_valid(self, form):
        excel_file = form.cleaned_data['excel_file']
        wb = load_workbook(filename=excel_file)
        sheet_name = 'waste'
        if sheet_name in wb.sheetnames:
            ws = wb[sheet_name]
        else:
            return self.form_invalid(form)

        with transaction.atomic():
            for row in ws.iter_rows(min_row=2, values_only=True):
                company_name = row[0]
                if company_name:
                    company, created = Company.objects.get_or_create(name=company_name)
                    Waste.objects.create(
                        company=company,
                        month=row[1],
                        year=row[2],
                        emission_type=row[3],
                        emission_scope=row[4],
                        waste_name=row[5],
                        quantity_recycled=row[6],
                        quantity_disposed=row[7],
                        quantity_land_filled=row[8],
                        emission_factor=row[9],
                    )
                else:

                    pass

        return super().form_valid(form)
